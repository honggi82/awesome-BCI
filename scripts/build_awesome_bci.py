import csv
import html
import json
import math
import re
import shutil
import time
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import requests
from docx import Document


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
PAPER_DIR = ROOT / "paper"
START_YEAR = 2000
END_YEAR = date.today().year
YEARS = list(range(START_YEAR, END_YEAR + 1))
YEAR_RANGE_TEXT = f"{START_YEAR}-{END_YEAR}"
YEAR_FILE_STEM = f"{START_YEAR}_{END_YEAR}"
PAPERS_JSON = f"papers_{YEAR_FILE_STEM}.json"
PAPERS_CSV = f"papers_{YEAR_FILE_STEM}.csv"
CANDIDATES_JSON = f"candidates_top500_{YEAR_FILE_STEM}.json"
CANDIDATES_CSV = f"candidates_top500_{YEAR_FILE_STEM}.csv"
TAXONOMY_CSV = f"papers_taxonomy_{YEAR_FILE_STEM}.csv"
TARGET_PER_YEAR = 100
CANDIDATES_PER_YEAR = 500

S2_BULK_URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
S2_FIELDS = ",".join([
    "paperId",
    "title",
    "year",
    "authors",
    "venue",
    "publicationVenue",
    "publicationDate",
    "citationCount",
    "influentialCitationCount",
    "abstract",
    "url",
    "externalIds",
    "openAccessPdf",
    "s2FieldsOfStudy",
    "publicationTypes",
])

QUERIES = [
    "brain computer interface",
    "brain machine interface",
    "BCI EEG",
    "motor imagery BCI",
    "SSVEP BCI",
    "P300 BCI",
    "brain computer interface rehabilitation",
    "invasive brain computer interface",
    "neural decoding brain computer interface",
    "deep learning brain computer interface",
]

RELEVANCE_PATTERNS = [
    r"\bbrain[- ]computer interface",
    r"\bbrain[- ]machine interface",
    r"\bBCI\b",
    r"\bSSVEP\b",
    r"\bP300\b",
    r"\bmotor imagery\b",
    r"\bneural decoding\b",
    r"\bintracortical\b",
    r"\belectrocorticography\b",
]

CATEGORIES = [
    ("Motor Imagery and Movement Decoding", ["motor imagery", "movement", "motor", "kinematic", "hand", "gait"]),
    ("SSVEP, P300, and ERP Spellers", ["ssvep", "p300", "erp", "speller", "steady state", "visual evoked"]),
    ("Rehabilitation and Neuroprosthetics", ["rehabilitation", "stroke", "prosthe", "exoskeleton", "restoration", "therapy"]),
    ("Invasive and Implantable Interfaces", ["invasive", "intracortical", "implant", "electrocorticography", "ecog", "microelectrode"]),
    ("Deep Learning and Representation Learning", ["deep learning", "convolution", "transformer", "graph neural", "domain adaptation", "self supervised"]),
    ("EEG Signal Processing and Datasets", ["eeg", "artifact", "signal processing", "dataset", "benchmark", "classification"]),
    ("Speech, Language, and Communication BCIs", ["speech", "language", "communication", "typing", "text", "decoding words"]),
    ("Hybrid, Affective, and Closed-loop BCIs", ["hybrid", "affective", "closed-loop", "closed loop", "neurofeedback", "adaptive"]),
]

TAXONOMY_TRENDS = {
    "Motor Imagery and Movement Decoding": [
        "The field is moving from subject-specific pipelines toward cross-subject, calibration-light, and transfer-learning decoders for EEG motor imagery.",
        "Deep CNN, temporal convolution, graph, attention, and large EEG representation models are increasingly used to improve robustness under noisy and low-data conditions.",
        "Application work is expanding from binary hand imagery toward gait, lower-limb control, soft robotics, virtual feedback, and rehabilitation-oriented closed-loop use.",
    ],
    "SSVEP, P300, and ERP Spellers": [
        "Research is concentrating on high-speed, many-target communication systems with lower calibration burden and more stable target recognition.",
        "Training-free and adaptive spatial filtering, task-discriminant component analysis, and deep neural decoders are prominent directions for SSVEP/P300 reliability.",
        "Hybrid paradigms that combine SSVEP, P300, RSVP, EOG, or augmented/virtual reality interfaces are becoming a practical route to richer command sets.",
    ],
    "Rehabilitation and Neuroprosthetics": [
        "The dominant trend is integration of BCI with robotic gloves, exoskeletons, FES, VR, and task-oriented therapy for post-stroke and motor impairment rehabilitation.",
        "Studies increasingly ask whether BCI training transfers to activities of daily living rather than only improving offline decoding accuracy.",
        "Recent work points toward home-use, patient-centered protocols, multimodal feedback, and combined motor-cognitive-affective rehabilitation.",
    ],
    "Invasive and Implantable Interfaces": [
        "Invasive BCI research is shifting toward high-bandwidth, stable, long-term decoding for movement, communication, and sensory feedback.",
        "Key engineering themes include wireless operation, power efficiency, signal longevity, surgical risk, and reliability outside tightly controlled laboratory sessions.",
        "Clinical translation is increasingly tied to home use, user safety, tactile feedback, speech decoding, and realistic functional tasks.",
    ],
    "Deep Learning and Representation Learning": [
        "Deep learning work is moving beyond single-dataset CNN classifiers toward temporal, spectral, graph, transformer, and attention-based architectures.",
        "A major trend is representation learning that can transfer across users, sessions, headsets, and BCI paradigms with less subject-specific calibration.",
        "Interpretability, uncertainty, robustness to artifacts, and benchmark comparability are becoming as important as peak classification accuracy.",
    ],
    "EEG Signal Processing and Datasets": [
        "This taxonomy emphasizes reproducible preprocessing, artifact handling, channel selection, spatial filtering, and benchmark datasets for EEG-based BCI.",
        "The field is gradually shifting from isolated algorithm papers toward shared datasets, standardized evaluation, and metadata-aware comparisons.",
        "Hybrid EEG/fNIRS, transfer learning, and open benchmark resources are recurring themes for improving generalization and clinical relevance.",
    ],
    "Speech, Language, and Communication BCIs": [
        "Communication BCI is expanding from spelling paradigms toward imagined speech, decoded language, and higher-bandwidth text production.",
        "Both invasive and non-invasive studies are exploring more naturalistic communication, including speech motor cortex decoding and inner-speech EEG datasets.",
        "The central challenge remains preserving accuracy, latency, vocabulary size, and user autonomy in real-world assistive communication.",
    ],
    "Hybrid, Affective, and Closed-loop BCIs": [
        "Hybrid BCI combines multiple signals or paradigms to improve reliability, command diversity, and asynchronous control.",
        "Closed-loop and neurofeedback work is increasingly focused on user adaptation, mental-state awareness, fatigue, affect, and training protocols.",
        "The trend is toward systems that adapt to the user over time rather than treating decoding as a one-shot offline classification problem.",
    ],
    "General BCI Methods and Systems": [
        "General BCI work is consolidating definitions, system architectures, evaluation principles, and long-term challenges across invasive and non-invasive approaches.",
        "Recent surveys increasingly emphasize translation, usability, ethics, safety, reproducibility, and the gap between laboratory performance and real-world use.",
        "This area functions as the conceptual bridge between signal processing, neural engineering, clinical deployment, and human-centered design.",
    ],
}

IMPORTANT_VENUES = [
    "nature", "science", "cell", "neuron", "nature biomedical engineering",
    "nature neuroscience", "nature communications", "science robotics",
    "journal of neural engineering", "neuroimage", "ieee transactions",
    "ieee trans", "frontiers in neuroscience", "frontiers in neurorobotics",
    "brain", "npj", "plos", "elife", "neural networks",
]


def norm_text(value):
    return re.sub(r"\s+", " ", value or "").strip()


def safe_slug(value):
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value[:80] or "paper"


def paper_key(paper):
    ext = paper.get("externalIds") or {}
    for key in ("DOI", "ArXiv", "PubMed", "CorpusId"):
        if ext.get(key):
            return f"{key}:{ext[key]}"
    return paper.get("paperId") or paper.get("url") or paper.get("title", "")


def is_relevant(paper):
    title = paper.get("title") or ""
    abstract = paper.get("abstract") or ""
    title_matches = title_relevance_count(paper)
    abstract_matches = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, abstract, re.I))
    return title_matches >= 1 or abstract_matches >= 2


def title_relevance_count(paper):
    title = paper.get("title") or ""
    return sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, title, re.I))


def venue_name(paper):
    venue = paper.get("venue") or ""
    pv = paper.get("publicationVenue") or {}
    return norm_text(venue or pv.get("name") or "")


def author_text(paper, max_authors=6):
    authors = paper.get("authors") or []
    names = [norm_text(a.get("name", "")) for a in authors if a.get("name")]
    if len(names) > max_authors:
        return ", ".join(names[:max_authors]) + ", et al."
    return ", ".join(names)


def category_for(paper):
    text = f"{paper.get('title') or ''} {paper.get('abstract') or ''}".lower()
    for category, needles in CATEGORIES:
        if any(n in text for n in needles):
            return category
    return "General BCI Methods and Systems"


def primary_link(paper):
    ext = paper.get("externalIds") or {}
    if ext.get("DOI"):
        return f"https://doi.org/{ext['DOI']}"
    if ext.get("ArXiv"):
        return f"https://arxiv.org/abs/{ext['ArXiv']}"
    return paper.get("url") or ""


def importance_score(paper):
    """Transparent metadata score used to reduce 500 candidates to 100 papers."""
    title = paper.get("title") or ""
    abstract = paper.get("abstract") or ""
    venue = venue_name(paper)
    text = f"{title} {abstract}".lower()
    venue_l = venue.lower()
    citations = int(paper.get("citationCount") or 0)
    influential = int(paper.get("influentialCitationCount") or 0)
    score = math.log1p(citations) * 22.0 + math.log1p(influential) * 18.0
    reasons = [f"citations={citations}", f"influential={influential}"]

    if any(v in venue_l for v in IMPORTANT_VENUES):
        score += 10.0
        reasons.append("recognized venue")
    if re.search(r"\b(review|survey|meta-analysis|systematic review)\b", text):
        score += 7.0
        reasons.append("review/survey")
    if re.search(r"\b(dataset|benchmark|competition|open data)\b", text):
        score += 5.0
        reasons.append("dataset/benchmark")
    if re.search(r"\b(clinical|stroke|rehabilitation|prosthe|paralysis|patient)\b", text):
        score += 5.0
        reasons.append("clinical/rehab relevance")
    if re.search(r"\b(invasive|intracortical|implant|electrocorticography|ecog)\b", text):
        score += 5.0
        reasons.append("invasive/high-bandwidth BCI")
    if re.search(r"\b(deep learning|transformer|self-supervised|domain adaptation|foundation model)\b", text):
        score += 4.0
        reasons.append("modern ML method")
    match_count = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, text, re.I))
    if match_count:
        score += min(8.0, match_count * 1.5)
        reasons.append(f"BCI term matches={match_count}")
    title_match_count = sum(1 for pattern in RELEVANCE_PATTERNS if re.search(pattern, title, re.I))
    if title_match_count:
        score += min(6.0, title_match_count * 2.0)
        reasons.append(f"title BCI matches={title_match_count}")
    if paper.get("openAccessPdf"):
        score += 1.0
        reasons.append("open PDF metadata")
    return round(score, 3), "; ".join(reasons)


def fetch_year_query(year, query, max_pages=2):
    params = {
        "query": query,
        "year": str(year),
        "fields": S2_FIELDS,
        "sort": "citationCount:desc",
    }
    out = []
    token = None
    for _ in range(max_pages):
        if token:
            params["token"] = token
        resp = requests.get(S2_BULK_URL, params=params, timeout=60)
        if resp.status_code == 429:
            time.sleep(8)
            resp = requests.get(S2_BULK_URL, params=params, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        out.extend(data.get("data") or [])
        token = data.get("token")
        if not token:
            break
        time.sleep(1.0)
    return out


def collect_papers():
    selected = {}
    all_candidates = {}
    for year in YEARS:
        merged = {}
        for query in QUERIES:
            print(f"[collect] {year} :: {query}", flush=True)
            try:
                for paper in fetch_year_query(year, query):
                    if paper.get("year") != year:
                        continue
                    if not paper.get("title") or not is_relevant(paper):
                        continue
                    merged[paper_key(paper)] = paper
            except Exception as exc:
                print(f"[warn] {year} {query}: {exc}", flush=True)
            time.sleep(1.0)

        ranked = sorted(
            merged.values(),
            key=lambda p: (
                importance_score(p)[0],
                int(p.get("citationCount") or 0),
                int(p.get("influentialCitationCount") or 0),
                p.get("title") or "",
            ),
            reverse=True,
        )
        candidate_pool = ranked[:CANDIDATES_PER_YEAR]
        citation_ranked = sorted(
            candidate_pool,
            key=lambda p: (
                int(p.get("citationCount") or 0),
                int(p.get("influentialCitationCount") or 0),
                importance_score(p)[0],
                p.get("title") or "",
            ),
            reverse=True,
        )
        selected_pool = citation_ranked[:TARGET_PER_YEAR]
        all_candidates[year] = [normalize_paper(p, year, i + 1, candidate=True) for i, p in enumerate(candidate_pool)]
        selected[year] = [normalize_paper(p, year, i + 1) for i, p in enumerate(selected_pool)]
        print(
            f"[collect] {year}: selected {len(selected[year])}/{TARGET_PER_YEAR} "
            f"by citations from top {len(candidate_pool)}/{min(CANDIDATES_PER_YEAR, len(ranked))} candidates "
            f"({len(ranked)} relevant records)",
            flush=True,
        )
    return selected, all_candidates


def normalize_paper(paper, year, rank, candidate=False):
    ext = paper.get("externalIds") or {}
    oa = paper.get("openAccessPdf") or {}
    fields = paper.get("s2FieldsOfStudy") or []
    score, reasons = importance_score(paper)
    return {
        "year": year,
        "rank": rank,
        "candidateRank": rank if candidate else "",
        "selectionRank": "" if candidate else rank,
        "importanceScore": score,
        "importanceReasons": reasons,
        "paperId": paper.get("paperId", ""),
        "title": norm_text(paper.get("title", "")),
        "authors": author_text(paper),
        "venue": venue_name(paper),
        "publicationDate": paper.get("publicationDate") or "",
        "citationCount": int(paper.get("citationCount") or 0),
        "influentialCitationCount": int(paper.get("influentialCitationCount") or 0),
        "category": category_for(paper),
        "abstract": norm_text(paper.get("abstract", "")),
        "doi": ext.get("DOI", ""),
        "arxiv": ext.get("ArXiv", ""),
        "pubmed": str(ext.get("PubMed", "")),
        "url": primary_link(paper),
        "semanticScholarUrl": paper.get("url", ""),
        "openAccessPdf": oa.get("url", "") if isinstance(oa, dict) else "",
        "fieldsOfStudy": "; ".join(sorted({f.get("category", "") for f in fields if f.get("category")})),
        "candidate": candidate,
    }


def write_json_csv(selected, candidates):
    flat = [paper for year in YEARS for paper in selected.get(year, [])]
    candidate_flat = [paper for year in YEARS for paper in candidates.get(year, [])]
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / PAPERS_JSON).open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "target_per_year": TARGET_PER_YEAR,
            "papers": flat,
        }, f, ensure_ascii=False, indent=2)
    with (DATA_DIR / CANDIDATES_JSON).open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "candidates": candidate_flat,
        }, f, ensure_ascii=False, indent=2)
    fields = list(flat[0].keys()) if flat else []
    candidate_fields = list(candidate_flat[0].keys()) if candidate_flat else fields
    with (DATA_DIR / PAPERS_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flat)
    with (DATA_DIR / CANDIDATES_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=candidate_fields)
        writer.writeheader()
        writer.writerows(candidate_flat)
    for year in YEARS:
        rows = selected.get(year, [])
        with (DATA_DIR / f"papers_{year}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        candidate_rows = candidates.get(year, [])
        with (DATA_DIR / f"candidates_top500_{year}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=candidate_fields)
            writer.writeheader()
            writer.writerows(candidate_rows)
    return flat


def year_stats(flat):
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    stats = {}
    for year, rows in by_year.items():
        stats[year] = {
            "count": len(rows),
            "citations": sum(p["citationCount"] for p in rows),
            "influential": sum(p["influentialCitationCount"] for p in rows),
            "top": rows[0] if rows else None,
        }
    return stats


def category_stats(flat):
    return Counter(p["category"] for p in flat)


def md_link(label, url):
    label = label.replace("|", "\\|")
    return f"[{label}]({url})" if url else label


def first_sentence(value, fallback="Metadata-only record; no abstract sentence was available."):
    text = norm_text(value)
    if not text:
        return fallback
    parts = re.split(r"(?<=[.!?])\s+", text)
    return parts[0][:360].rstrip()


def method_tags(p):
    text = f"{p.get('title', '')} {p.get('abstract', '')}".lower()
    tags = []
    checks = [
        ("review", r"\b(review|survey|meta-analysis|systematic review)\b"),
        ("dataset/benchmark", r"\b(dataset|benchmark|competition|open data)\b"),
        ("clinical/rehab", r"\b(clinical|stroke|rehabilitation|prosthe|patient|paralysis)\b"),
        ("invasive", r"\b(invasive|intracortical|implant|electrocorticography|ecog)\b"),
        ("deep learning", r"\b(deep learning|cnn|convolution|transformer|graph neural|self-supervised|domain adaptation)\b"),
        ("communication", r"\b(speech|language|speller|typing|communication)\b"),
        ("closed-loop", r"\b(closed-loop|closed loop|neurofeedback|adaptive)\b"),
    ]
    for label, pattern in checks:
        if re.search(pattern, text):
            tags.append(label)
    return tags[:4] or ["BCI method"]


def enrich_paper(p):
    """Add reproducible interpretation fields from title, abstract, and metadata."""
    abstract = p.get("abstract", "")
    idea = first_sentence(abstract, f"Positions {p.get('title', 'this paper')} within {p.get('category', 'BCI research')}.")
    tags = method_tags(p)
    strengths = []
    if p.get("citationCount", 0) >= 100:
        strengths.append(f"high citation signal ({p['citationCount']:,})")
    if p.get("influentialCitationCount", 0) >= 10:
        strengths.append(f"influential citation signal ({p['influentialCitationCount']:,})")
    if "recognized venue" in p.get("importanceReasons", ""):
        strengths.append("recognized venue")
    if p.get("openAccessPdf"):
        strengths.append("open-access PDF metadata")
    if not strengths:
        strengths.append("selected by citation count from the audited BCI candidate pool")

    limitations = []
    if not abstract:
        limitations.append("abstract unavailable in metadata")
    if not p.get("venue"):
        limitations.append("venue missing in metadata")
    if p.get("year", 0) >= 2025:
        limitations.append("recent work may be under-cited")
    if p.get("citationCount", 0) < 25:
        limitations.append("limited citation history")
    if not p.get("openAccessPdf"):
        limitations.append("PDF link not available from metadata")
    if not limitations:
        limitations.append("metadata-level appraisal; full PDF review still needed")

    enriched = dict(p)
    enriched["keyIdea"] = idea
    enriched["strengths"] = "; ".join(strengths[:3])
    enriched["limitations"] = "; ".join(limitations[:3])
    enriched["methodTags"] = "; ".join(tags)
    enriched["paperLink"] = p.get("url") or p.get("semanticScholarUrl") or ""
    return enriched


def enriched_flat(flat):
    return [enrich_paper(p) for p in flat]


def category_groups(flat):
    groups = defaultdict(list)
    for p in enriched_flat(flat):
        groups[p["category"]].append(p)
    for rows in groups.values():
        rows.sort(key=lambda p: (p["citationCount"], p["influentialCitationCount"], p["importanceScore"]), reverse=True)
    return groups


def taxonomy_trends(category):
    return TAXONOMY_TRENDS.get(category, TAXONOMY_TRENDS["General BCI Methods and Systems"])


def write_taxonomy_dataset(flat):
    rows = []
    for category, papers in sorted(category_groups(flat).items()):
        for idx, p in enumerate(papers, 1):
            row = dict(p)
            row["taxonomyRank"] = idx
            row["researchTrend"] = " ".join(taxonomy_trends(category))
            rows.append(row)
    if not rows:
        return
    fields = [
        "category", "taxonomyRank", "year", "title", "authors", "venue", "publicationDate",
        "citationCount", "influentialCitationCount", "importanceScore", "researchTrend", "methodTags",
        "keyIdea", "strengths", "limitations", "paperLink", "semanticScholarUrl",
        "openAccessPdf", "doi", "arxiv", "pubmed", "fieldsOfStudy",
    ]
    with (DATA_DIR / TAXONOMY_CSV).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def readme_taxonomy_table(rows, total_count):
    out = [
        '<table width="100%">',
        "<colgroup>",
        '<col width="5%">',
        '<col width="22%">',
        '<col width="13%">',
        '<col width="30%">',
        '<col width="15%">',
        '<col width="15%">',
        "</colgroup>",
        "<thead>",
        "<tr>",
        '<th align="right">Rank</th>',
        "<th>Paper</th>",
        "<th>Meta</th>",
        "<th>Key idea</th>",
        "<th>Strengths</th>",
        "<th>Limitations</th>",
        "</tr>",
        "</thead>",
        "<tbody>",
    ]
    for idx, p in enumerate(rows, 1):
        title = html.escape(p["title"])
        link = html.escape(p["paperLink"])
        paper = f'<a href="{link}">{title}</a>' if link else title
        authors = html.escape(p["authors"] or "Unknown authors")
        venue = html.escape(p["venue"] or "Unknown venue")
        out.extend([
            "<tr>",
            f'<td align="right" width="5%">{idx}</td>',
            f'<td width="22%">{paper}<br><sub>{authors}</sub></td>',
            f'<td width="13%">{p["year"]}<br>{venue}<br>{p["citationCount"]:,} citations</td>',
            f'<td width="30%">{html.escape(p["keyIdea"])}</td>',
            f'<td width="15%">{html.escape(p["strengths"])}</td>',
            f'<td width="15%">{html.escape(p["limitations"])}</td>',
            "</tr>",
        ])
    if total_count > len(rows):
        out.extend([
            "<tr>",
            f'<td colspan="6">See the website and taxonomy CSV for all {total_count} papers.</td>',
            "</tr>",
        ])
    out.extend(["</tbody>", "</table>"])
    return out


def write_readme(flat):
    stats = year_stats(flat)
    cats = category_stats(flat)
    groups = category_groups(flat)
    lines = [
        "# Awesome BCI",
        "",
        "[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)",
        "",
        "A taxonomy-first, citation-ranked map of recent Brain-Computer Interface (BCI) research.",
        "",
        f"Generated on {date.today().isoformat()} from free public Semantic Scholar metadata. The current edition investigates up to {CANDIDATES_PER_YEAR} BCI-related candidate papers per year for {YEAR_RANGE_TEXT}, keeps an audited candidate pool, selects the top {TARGET_PER_YEAR} papers per year by citation count, and reorganizes the final {len(flat):,} papers by research taxonomy.",
        "",
        "## Project Links",
        "",
        "- Website: https://honggi82.github.io/awesome-BCI/",
        f"- Selected dataset: `data/{PAPERS_CSV}`",
        f"- Taxonomy dataset with paper-level ideas, strengths, and limitations: `data/{TAXONOMY_CSV}`",
        f"- Candidate pool: `data/{CANDIDATES_CSV}`",
        "- English review draft: `paper/review_en.html`, `paper/review_en.docx`",
        "- Korean review draft: `paper/review_ko.html`",
        "",
        "## Taxonomy Overview",
        "",
    ]
    for cat, count in cats.most_common():
        lines.append(f"- **{cat}**: {count} papers")

    lines.extend(["", "## Taxonomy Collections", ""])
    for cat, _ in cats.most_common():
        rows = groups[cat]
        top = rows[:30]
        years = sorted({p["year"] for p in rows})
        citations = sum(p["citationCount"] for p in rows)
        lines.extend([
            f"### {cat}",
            "",
            f"- Papers selected: **{len(rows)}**",
            f"- Years covered: **{years[0]}-{years[-1]}**",
            f"- Citation count in selected set: **{citations:,}**",
            "- Main research trends:",
            *[f"  - {trend}" for trend in taxonomy_trends(cat)],
            "",
            "<details>",
            f"<summary>Show representative papers for {cat}</summary>",
            "",
        ])
        lines.extend(readme_taxonomy_table(top, len(rows)))
        lines.extend(["", "</details>", ""])

    lines.extend([
        "## Yearly Coverage",
        "",
        "| Year | Selected papers | Citation count | Top paper |",
        "| ---: | ---: | ---: | --- |",
    ])
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    for year in YEARS:
        rows = by_year.get(year, [])
        top = rows[0] if rows else None
        top_link = md_link(top["title"], top["url"]) if top else "n/a"
        lines.append(
            f"| {year} | {len(rows)} | {stats.get(year, {}).get('citations', 0):,} | {top_link} |"
        )
    lines.extend([
        "## Method",
        "",
        "The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and reduced to a maximum of 500 candidates per year. Importance scoring is retained for candidate auditing and combines log-scaled citation count, log-scaled influential citation count, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive/high-bandwidth interfaces, and modern ML methods. The final awesome list selects the top 100 papers per year by citation count from the audited candidate pool.",
        "",
        "## Caveats",
        "",
        f"- Citation counts favor older papers and may under-rank recent {END_YEAR} work.",
        "- Metadata search is not equivalent to a full systematic review of PDFs.",
        "- Some venues and publication dates are missing in upstream metadata.",
    ])
    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def category_summary(category, rows):
    top_tags = Counter()
    for p in rows:
        for tag in p.get("methodTags", "").split("; "):
            if tag:
                top_tags[tag] += 1
    lead = rows[0] if rows else {}
    return {
        "count": len(rows),
        "years": f"{min(p['year'] for p in rows)}-{max(p['year'] for p in rows)}" if rows else "",
        "citations": sum(p["citationCount"] for p in rows),
        "top": lead.get("title", "n/a"),
        "tags": ", ".join(tag for tag, _ in top_tags.most_common(4)) or "BCI method",
        "trends": taxonomy_trends(category),
    }


def paper_card(p, taxonomy_rank):
    title = html.escape(p["title"])
    link = html.escape(p["paperLink"])
    semantic = html.escape(p.get("semanticScholarUrl") or "")
    pdf = html.escape(p.get("openAccessPdf") or "")
    paper_link = f'<a href="{link}">Paper</a>' if link else ""
    semantic_link = f'<a href="{semantic}">Semantic Scholar</a>' if semantic else ""
    pdf_link = f'<a href="{pdf}">PDF</a>' if pdf else ""
    links = " ".join(x for x in [paper_link, semantic_link, pdf_link] if x) or "No link"
    return f"""
      <article class="paper-card" data-year="{p['year']}" data-citations="{p['citationCount']}">
        <div class="paper-rank">#{taxonomy_rank}</div>
        <div class="paper-body">
          <h3>{f'<a href="{link}">{title}</a>' if link else title}</h3>
          <p class="authors">{html.escape(p["authors"] or "Unknown authors")}</p>
          <div class="meta">
            <span>{p["year"]}</span>
            <span>{html.escape(p["venue"] or "Unknown venue")}</span>
            <span>{p["citationCount"]:,} citations</span>
            <span>{p["influentialCitationCount"]:,} influential</span>
            <span>score {p["importanceScore"]}</span>
          </div>
          <p><strong>Key idea:</strong> {html.escape(p["keyIdea"])}</p>
          <div class="assessment">
            <p><strong>Strengths:</strong> {html.escape(p["strengths"])}</p>
            <p><strong>Limitations:</strong> {html.escape(p["limitations"])}</p>
          </div>
          <p class="tags">{html.escape(p["methodTags"])}</p>
          <p class="links">{links}</p>
        </div>
      </article>
    """


def taxonomy_section(category, rows):
    slug = safe_slug(category)
    summary = category_summary(category, rows)
    cards = "\n".join(paper_card(p, idx) for idx, p in enumerate(rows, 1))
    return f"""
    <section id="{slug}" class="taxonomy-section" data-category="{slug}">
      <details>
        <summary>
          <span class="summary-title">{html.escape(category)}</span>
          <span class="category-count">{summary['count']} papers</span>
          <span class="category-years">{summary['years']}</span>
          <span class="category-citations">{summary['citations']:,} citations</span>
        </summary>
        <div class="section-intro">
          <p><strong>Representative emphasis:</strong> {html.escape(summary['tags'])}</p>
          <p><strong>Top-ranked paper:</strong> <span class="top-paper">{html.escape(summary['top'])}</span></p>
          <div class="trend-box">
            <strong>Main research trends</strong>
            <ul>{''.join(f'<li>{html.escape(trend)}</li>' for trend in summary['trends'])}</ul>
          </div>
        </div>
        <div class="paper-list">{cards}</div>
      </details>
    </section>
    """


def write_site(flat):
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "assets").mkdir(exist_ok=True)
    (DOCS_DIR / "data").mkdir(exist_ok=True)
    (DOCS_DIR / "paper").mkdir(exist_ok=True)
    groups = category_groups(flat)
    cats = category_stats(flat)
    total_cites = sum(p["citationCount"] for p in flat)
    start_year_options = "\n".join(
        f'<option value="{year}"{" selected" if year == min(YEARS) else ""}>{year}</option>'
        for year in YEARS
    )
    end_year_options = "\n".join(
        f'<option value="{year}"{" selected" if year == max(YEARS) else ""}>{year}</option>'
        for year in YEARS
    )
    year_filter_script = """
  <script>
    (() => {
      const startSelect = document.getElementById("startYear");
      const endSelect = document.getElementById("endYear");
      const resetButton = document.getElementById("resetYears");
      const rangeStatus = document.getElementById("rangeStatus");
      const statPapers = document.getElementById("statPapers");
      const statYears = document.getElementById("statYears");
      const statCitations = document.getElementById("statCitations");
      const statCategories = document.getElementById("statCategories");
      const defaultStart = startSelect.value;
      const defaultEnd = endSelect.value;
      const validYears = Array.from(startSelect.options).map(option => option.value);

      function formatNumber(value) {
        return Number(value).toLocaleString("en-US");
      }

      function yearRangeText(years) {
        if (!years.length) return "No years";
        const sorted = [...new Set(years)].sort((a, b) => a - b);
        return sorted[0] === sorted[sorted.length - 1]
          ? String(sorted[0])
          : `${sorted[0]}-${sorted[sorted.length - 1]}`;
      }

      function setFromUrl() {
        const params = new URLSearchParams(window.location.search);
        const from = params.get("from");
        const to = params.get("to");
        if (validYears.includes(from)) startSelect.value = from;
        if (validYears.includes(to)) endSelect.value = to;
      }

      function syncUrl(start, end) {
        const url = new URL(window.location.href);
        if (String(start) === defaultStart && String(end) === defaultEnd) {
          url.searchParams.delete("from");
          url.searchParams.delete("to");
        } else {
          url.searchParams.set("from", start);
          url.searchParams.set("to", end);
        }
        window.history.replaceState(null, "", url);
      }

      function applyYearFilter(sync = true) {
        let start = Number(startSelect.value);
        let end = Number(endSelect.value);
        if (start > end) {
          const previousStart = start;
          start = end;
          end = previousStart;
          startSelect.value = String(start);
          endSelect.value = String(end);
        }

        let totalPapers = 0;
        let totalCitations = 0;
        let activeCategories = 0;
        const activeYears = [];

        document.querySelectorAll(".taxonomy-section").forEach(section => {
          let sectionCount = 0;
          let sectionCitations = 0;
          const sectionYears = [];

          section.querySelectorAll(".paper-card").forEach(card => {
            const year = Number(card.dataset.year);
            const citations = Number(card.dataset.citations || 0);
            const visible = year >= start && year <= end;
            card.hidden = !visible;
            if (visible) {
              sectionCount += 1;
              sectionCitations += citations;
              sectionYears.push(year);
              activeYears.push(year);
            }
          });

          const hasPapers = sectionCount > 0;
          section.hidden = !hasPapers;
          const overview = document.querySelector(`.taxonomy-card[data-category="${section.dataset.category}"]`);
          if (overview) {
            overview.hidden = !hasPapers;
            const overviewCount = overview.querySelector(".overview-count");
            if (overviewCount) overviewCount.textContent = `${formatNumber(sectionCount)} papers`;
          }
          if (!hasPapers) return;

          activeCategories += 1;
          totalPapers += sectionCount;
          totalCitations += sectionCitations;
          section.querySelector(".category-count").textContent = `${formatNumber(sectionCount)} papers`;
          section.querySelector(".category-years").textContent = yearRangeText(sectionYears);
          section.querySelector(".category-citations").textContent = `${formatNumber(sectionCitations)} citations`;
          const topPaper = section.querySelector(".paper-card:not([hidden]) h3");
          const topPaperTarget = section.querySelector(".top-paper");
          if (topPaper && topPaperTarget) topPaperTarget.textContent = topPaper.textContent.trim();
        });

        statPapers.textContent = formatNumber(totalPapers);
        statYears.textContent = formatNumber(new Set(activeYears).size);
        statCitations.textContent = formatNumber(totalCitations);
        statCategories.textContent = formatNumber(activeCategories);
        rangeStatus.textContent = `${start}-${end} · ${formatNumber(totalPapers)} papers · ${formatNumber(activeCategories)} categories`;
        if (sync) syncUrl(start, end);
      }

      setFromUrl();
      applyYearFilter(false);
      startSelect.addEventListener("change", () => applyYearFilter(true));
      endSelect.addEventListener("change", () => applyYearFilter(true));
      resetButton.addEventListener("click", () => {
        startSelect.value = defaultStart;
        endSelect.value = defaultEnd;
        applyYearFilter(true);
      });
    })();
  </script>
"""
    sections = []
    for cat, _ in cats.most_common():
        sections.append(taxonomy_section(cat, groups[cat]))
    cat_cards = "\n".join(
        f"<a class='card taxonomy-card' data-category='{safe_slug(cat)}' href='#{safe_slug(cat)}'><strong>{html.escape(cat)}</strong><span class='overview-count'>{count} papers</span></a>"
        for cat, count in cats.most_common()
    )
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,">
  <title>Awesome BCI</title>
  <style>
    :root {{ color-scheme: light; --ink:#18212f; --muted:#5b6678; --line:#d9dee8; --accent:#0f766e; --accent2:#7c3aed; --bg:#f7f9fc; --panel:#ffffff; }}
    body {{ margin:0; font-family: Inter, Segoe UI, Arial, sans-serif; color:var(--ink); background:var(--bg); }}
    header {{ padding:54px 7vw 34px; background:linear-gradient(120deg,#e9fbf8,#eef2ff); border-bottom:1px solid var(--line); }}
    h1 {{ font-size:48px; margin:0 0 12px; letter-spacing:0; }}
    h2 {{ margin-top:36px; }}
    p {{ line-height:1.65; color:var(--muted); }}
    main {{ padding:28px 7vw 72px; }}
    .stats, .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; margin:24px 0; }}
    .filters {{ display:flex; flex-wrap:wrap; align-items:end; gap:12px; margin:24px 0; padding:14px; background:white; border:1px solid var(--line); border-radius:8px; }}
    .filter-field {{ display:grid; gap:6px; }}
    .filter-field label {{ font-weight:700; font-size:13px; color:#344255; }}
    select {{ min-width:104px; height:38px; border:1px solid var(--line); border-radius:8px; background:white; color:var(--ink); padding:0 10px; font:inherit; }}
    button {{ height:38px; border:1px solid #bfc8d8; border-radius:8px; background:#f6f8fb; color:var(--ink); padding:0 14px; font-weight:700; cursor:pointer; }}
    button:hover {{ background:#eef2f7; }}
    #rangeStatus {{ color:var(--muted); font-weight:700; min-height:38px; display:inline-flex; align-items:center; }}
    .figures {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; margin:24px 0; }}
    .figures img {{ width:100%; background:white; border:1px solid var(--line); border-radius:8px; }}
    .stat, .card {{ background:white; border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .stat strong {{ display:block; font-size:28px; color:var(--accent); }}
    .card span {{ display:block; margin-top:8px; color:var(--muted); }}
    nav a {{ display:inline-block; margin:0 12px 10px 0; color:var(--accent2); font-weight:600; }}
    .card {{ display:block; color:var(--ink); }}
    .taxonomy-section {{ margin-top:16px; }}
    details {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; }}
    summary {{ cursor:pointer; display:grid; grid-template-columns:minmax(260px,1fr) repeat(3, minmax(110px, auto)); gap:12px; align-items:center; padding:16px 18px; font-weight:700; }}
    .summary-title {{ color:var(--accent); }}
    .section-intro {{ padding:0 18px 14px; border-top:1px solid var(--line); }}
    .trend-box {{ margin-top:12px; padding:12px 14px; background:#f4faf8; border:1px solid #cfe7df; border-radius:8px; }}
    .trend-box ul {{ margin:8px 0 0; padding-left:20px; color:var(--muted); line-height:1.55; }}
    .paper-list {{ display:grid; gap:12px; padding:16px; background:#f9fbfd; }}
    .paper-card {{ display:grid; grid-template-columns:56px 1fr; gap:14px; padding:16px; background:white; border:1px solid var(--line); border-radius:8px; }}
    .paper-rank {{ font-weight:800; color:var(--accent2); }}
    .paper-card h3 {{ margin:0 0 6px; font-size:18px; line-height:1.35; }}
    .authors {{ margin:0 0 8px; }}
    .meta {{ display:flex; flex-wrap:wrap; gap:8px; margin:8px 0 10px; }}
    .meta span, .tags {{ display:inline-block; background:#eef2f7; border:1px solid #dce3ee; border-radius:999px; padding:5px 9px; color:#344255; font-size:13px; }}
    .assessment {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:8px; }}
    .links a {{ margin-right:12px; font-weight:700; }}
    a {{ color:#0f5f97; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    @media (max-width:760px) {{
      h1 {{ font-size:36px; }}
      summary {{ grid-template-columns:1fr; }}
      .paper-card {{ grid-template-columns:1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>Awesome BCI</h1>
    <p>A taxonomy-first map of Brain-Computer Interface research from {START_YEAR} through {END_YEAR}. Each year investigates up to {CANDIDATES_PER_YEAR} candidate papers, selects the top {TARGET_PER_YEAR}, and organizes the final papers by BCI research theme.</p>
    <nav>
      <a href="https://github.com/honggi82/awesome-BCI">README</a>
      <a href="data/{PAPERS_CSV}">CSV Dataset</a>
      <a href="data/{TAXONOMY_CSV}">Taxonomy CSV</a>
      <a href="data/{CANDIDATES_CSV}">Candidate Pool</a>
      <a href="paper/review_en.html">Review Paper</a>
      <a href="paper/review_ko.html">Korean Review</a>
    </nav>
  </header>
  <main>
    <div class="stats">
      <div class="stat"><strong id="statPapers">{len(flat)}</strong><span>selected papers</span></div>
      <div class="stat"><strong id="statYears">{len(YEARS)}</strong><span>years covered</span></div>
      <div class="stat"><strong id="statCitations">{total_cites:,}</strong><span>citation count total</span></div>
      <div class="stat"><strong id="statCategories">{len(cats)}</strong><span>topic categories</span></div>
    </div>
    <form class="filters" id="yearFilter">
      <div class="filter-field">
        <label for="startYear">Start year</label>
        <select id="startYear" name="from">{start_year_options}</select>
      </div>
      <div class="filter-field">
        <label for="endYear">End year</label>
        <select id="endYear" name="to">{end_year_options}</select>
      </div>
      <button type="button" id="resetYears">Reset</button>
      <span id="rangeStatus"></span>
    </form>
    <h2>Taxonomy</h2>
    <p>Each taxonomy section lists papers with publication year, journal or venue, citation count, main idea, strengths, limitations, and paper links. Sections are collapsed by default to keep the page scannable.</p>
    <div class="figures">
      <img src="assets/category_distribution.png" alt="Category distribution chart">
      <img src="assets/yearly_citations.png" alt="Yearly citation chart">
    </div>
    <div class="cards">{cat_cards}</div>
    {''.join(sections)}
  </main>
{year_filter_script}
</body>
</html>
"""
    (DOCS_DIR / "index.html").write_text(html_doc, encoding="utf-8")
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")


def write_charts(flat):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    assets = DOCS_DIR / "assets"
    assets.mkdir(exist_ok=True)

    cats = category_stats(flat).most_common()
    labels = [c for c, _ in cats][::-1]
    values = [v for _, v in cats][::-1]
    fig, ax = plt.subplots(figsize=(11, 6), dpi=160)
    ax.barh(labels, values, color="#0f766e")
    ax.set_xlabel("Selected papers")
    ax.set_title(f"BCI Paper Taxonomy, {YEAR_RANGE_TEXT}")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(assets / "category_distribution.png")
    plt.close(fig)

    stats = year_stats(flat)
    years = [y for y in YEARS if y in stats]
    citations = [stats[y]["citations"] for y in years]
    fig, ax = plt.subplots(figsize=(9, 5), dpi=160)
    ax.bar([str(y) for y in years], citations, color="#7c3aed")
    ax.set_ylabel("Citation count in selected set")
    ax.set_title("Yearly Citation Mass of Selected BCI Papers")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(assets / "yearly_citations.png")
    plt.close(fig)


def reference_line(p):
    authors = p["authors"] or "Unknown authors"
    venue = p["venue"] or "Unknown venue"
    link = p["url"] or p["semanticScholarUrl"]
    return f"{authors}. ({p['year']}). {p['title']}. {venue}. {link}"


def review_sections(flat, korean=False):
    stats = year_stats(flat)
    cats = category_stats(flat)
    top_by_year = [stats[y]["top"] for y in YEARS if stats.get(y, {}).get("top")]
    if korean:
        title = f"{YEAR_RANGE_TEXT}년 뇌-컴퓨터 인터페이스 연구 동향: 공개 메타데이터 기반 리뷰"
        abstract = (
            f"이 리뷰 초안은 {START_YEAR}년부터 {END_YEAR}년까지의 Brain-Computer Interface(BCI) 연구를 "
            f"연도별 최대 {CANDIDATES_PER_YEAR}편의 후보로 조사하고 인용회수 기준으로 {TARGET_PER_YEAR}편씩 선별해 정리한다. 선별은 무료 공개 Semantic Scholar 메타데이터를 "
            "사용했으며, 검색어 기반 후보군을 연도 필터, 강화된 BCI 관련성 필터, 중복 제거, 후보 감사용 중요도 점수화로 처리했다. "
            "결과는 운동상상/운동 디코딩, SSVEP/P300/ERP, 재활과 신경보철, 침습형 인터페이스, 딥러닝, EEG 신호처리, "
            "언어/의사소통 BCI, 폐루프/하이브리드 BCI로 나뉜다."
        )
        methods = (
            "방법: 각 연도에 대해 BCI 관련 질의를 Semantic Scholar Academic Graph bulk search에 보내고, "
            "제목 또는 초록에 BCI 관련 핵심 표현이 있는 논문만 남겼다. DOI, arXiv, PubMed, CorpusId, paperId 순서로 "
            f"중복을 제거했다. 이후 연도별 최대 {CANDIDATES_PER_YEAR}편의 후보 풀을 만들고, 그 안에서 인용회수 상위 {TARGET_PER_YEAR}편을 최종 목록에 사용했다. "
            "영향력 있는 인용 수와 중요도 점수는 동률 처리와 감사용 보조 신호로 유지했다. 중요도 점수는 로그 변환 인용 수, 영향력 있는 인용 수, 주요 venue 신호, BCI 핵심어 밀도, 리뷰/서베이, 데이터셋/벤치마크, "
            f"임상/재활 관련성, 침습형 고대역폭 BCI, 최신 머신러닝 방법 보너스를 합산했다. {END_YEAR}년은 {date.today().isoformat()} 현재의 부분 연도라는 점에 유의해야 한다."
        )
        trends_intro = "주요 경향은 다음과 같다."
        caveat = (
            "한계: 이 문서는 전문 PDF를 모두 읽은 체계적 문헌고찰이 아니라 메타데이터 기반 리뷰 초안이다. "
            "인용 수는 최신 논문에 불리하며, 일부 논문의 venue/date 정보는 원천 데이터에서 누락될 수 있다."
        )
        conclusion = (
            f"결론적으로 {START_YEAR}년 이후 BCI 연구는 딥러닝 기반 EEG 디코딩과 벤치마크, 재활 응용, 침습형 고성능 디코딩, "
            "사용자 친화적 의사소통 시스템 사이에서 빠르게 확장되고 있다. 향후 리뷰에서는 실제 PDF 기반 품질 평가, "
            "임상 전환성, 데이터셋 재현성, 장기 안정성, 안전성과 윤리 문제를 함께 검토해야 한다."
        )
    else:
        title = f"Brain-Computer Interface Research from {START_YEAR} to {END_YEAR}: A Metadata-Driven Review"
        abstract = (
            f"This draft review maps Brain-Computer Interface (BCI) research from {START_YEAR} through {END_YEAR}, investigating up to "
            f"{CANDIDATES_PER_YEAR} candidate papers per year from free public Semantic Scholar metadata and selecting {TARGET_PER_YEAR} papers per year by citation count. Candidate papers were retrieved with BCI-related "
            "queries, filtered by target year and strengthened BCI relevance terms, deduplicated, and scored for candidate auditing. The resulting "
            "collection highlights work on motor imagery and movement decoding, SSVEP/P300/ERP systems, rehabilitation and "
            "neuroprosthetics, invasive interfaces, deep learning, EEG signal processing, speech and communication BCIs, and "
            "hybrid or closed-loop systems."
        )
        methods = (
            "Methods: For each year, BCI-oriented queries were sent to the Semantic Scholar Academic Graph bulk search endpoint. "
            "Records were retained when their title or abstract matched BCI relevance expressions, deduplicated by DOI, arXiv, "
            f"PubMed, CorpusId, or paperId, and reduced to at most {CANDIDATES_PER_YEAR} candidate papers per year. The final {TARGET_PER_YEAR} papers per year were selected by citation count, with influential citation count and the metadata importance score retained as tie-breakers and audit signals. The importance score combines log-scaled citations, log-scaled influential citations, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive high-bandwidth BCIs, and modern machine-learning methods. The year {END_YEAR} should be interpreted as a partial year as of {date.today().isoformat()}."
        )
        trends_intro = "The main metadata-level trends are as follows."
        caveat = (
            "Limitations: this is a metadata-driven review draft rather than a full systematic review of every PDF. Citation counts "
            f"favor older work, recent {END_YEAR} papers are structurally under-counted, and some venues or publication dates are missing upstream."
        )
        conclusion = (
            f"Overall, BCI research since {START_YEAR} is expanding across deep-learning EEG decoding, benchmarks and datasets, rehabilitation, "
            "high-performance invasive decoding, and usable communication systems. A full manuscript should next add PDF-level appraisal, "
            "clinical translation evidence, dataset reproducibility, long-term stability, safety, and ethics."
        )
    category_lines = [f"{cat}: {count}" for cat, count in cats.most_common()]
    year_lines = [
        f"{y}: {stats[y]['count']} papers, {stats[y]['citations']:,} citations in selected set, top paper: {stats[y]['top']['title']}"
        for y in YEARS if y in stats
    ]
    refs = [reference_line(p) for p in top_by_year]
    return title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs


def review_deep_dive(flat, korean=False):
    cats = category_stats(flat)
    stats = year_stats(flat)
    top_scored = sorted(flat, key=lambda p: p["importanceScore"], reverse=True)[:12]
    top_cited = sorted(flat, key=lambda p: p["citationCount"], reverse=True)[:12]
    leading_cat, leading_count = cats.most_common(1)[0]
    total_cites = sum(p["citationCount"] for p in flat)
    peak_year = max(stats, key=lambda y: stats[y]["citations"])
    newest_year = max(YEARS)

    if korean:
        findings = [
            f"선정된 {len(flat)}편은 총 {total_cites:,}회의 인용을 포함하며, 인용량은 {peak_year}년에 가장 높다.",
            f"가장 큰 축은 {leading_cat}({leading_count}편)으로, {START_YEAR}년 이후 BCI 연구가 여전히 운동 의도 해석과 운동 기능 보조를 중심으로 조직되어 있음을 보여준다.",
            f"{newest_year}년 논문은 부분 연도라 인용 수가 낮지만, foundation model, 장기 안정성, 고성능 침습형 디코딩, 임상 전환성 같은 주제가 두드러진다.",
            "비침습 EEG-BCI는 데이터셋/벤치마크와 딥러닝 방법론이 빠르게 늘었고, 침습형 BCI는 의사소통·운동 복원 성능을 실제 사용성 문제와 연결하는 방향으로 이동하고 있다.",
        ]
        category_discussion = [
            f"{cat}: {count}편. 이 범주는 최종 목록의 {count / len(flat):.1%}를 차지한다."
            for cat, count in cats.most_common()
        ]
        future = [
            "PDF 전문 기반의 임상근거 수준 평가와 risk-of-bias 코딩을 추가한다.",
            "데이터셋 공개 여부, 재현 코드, 피험자 수, 장기 안정성 지표를 별도 열로 정규화한다.",
            "후보 500편 풀에서 연도별 저인용 최신 논문의 잠재력을 전문가 검토로 보정한다.",
            "장애 당사자 중심 사용성, 안전성, 개인정보, 신경윤리 기준을 별도 taxonomy로 확장한다.",
        ]
        top_scored_heading = "메타데이터 중요도 점수 상위 논문(감사용)"
        top_cited_heading = "인용 수 상위 논문"
    else:
        findings = [
            f"The {len(flat)} selected papers account for {total_cites:,} citations in the selected set, with the largest citation mass in {peak_year}.",
            f"The dominant category is {leading_cat} ({leading_count} papers), indicating that movement intention decoding and motor assistance remain the organizing center of BCI research since {START_YEAR}.",
            f"Papers from {newest_year} are structurally citation-disadvantaged because the year is partial, but they surface emerging themes around foundation models, stability, invasive high-bandwidth decoding, and clinical translation.",
            "Non-invasive EEG-BCI work is increasingly shaped by datasets, benchmarks, and deep learning, while invasive BCI work is moving from peak decoding performance toward communication, autonomy, and usability constraints.",
        ]
        category_discussion = [
            f"{cat}: {count} papers, representing {count / len(flat):.1%} of the selected set."
            for cat, count in cats.most_common()
        ]
        future = [
            "Add PDF-level appraisal of clinical evidence and risk-of-bias indicators.",
            "Normalize dataset availability, released code, participant counts, and long-term stability metrics.",
            "Use expert review to compensate for low citation counts among very recent papers in the 500-candidate pools.",
            "Extend the taxonomy with user-centered usability, safety, privacy, and neuroethics criteria.",
        ]
        top_scored_heading = "Top Papers by Metadata Importance Score (Audit Signal)"
        top_cited_heading = "Top Papers by Citation Count"

    return {
        "findings": findings,
        "category_discussion": category_discussion,
        "future": future,
        "top_scored": top_scored,
        "top_cited": top_cited,
        "top_scored_heading": top_scored_heading,
        "top_cited_heading": top_cited_heading,
    }


def html_ranked_table(rows, metric):
    heading = "Importance" if metric == "importance" else "Citations"
    out = [
        "<table>",
        f"<thead><tr><th>Year</th><th>Rank</th><th>Paper</th><th>{heading}</th><th>Category</th></tr></thead>",
        "<tbody>",
    ]
    for p in rows:
        metric_value = p["importanceScore"] if metric == "importance" else p["citationCount"]
        link = f'<a href="{html.escape(p["url"])}">{html.escape(p["title"])}</a>' if p["url"] else html.escape(p["title"])
        out.append(
            f"<tr><td>{p['year']}</td><td>{p['rank']}</td><td>{link}</td>"
            f"<td>{metric_value}</td><td>{html.escape(p['category'])}</td></tr>"
        )
    out.extend(["</tbody>", "</table>"])
    return "\n".join(out)


def write_review_html(flat, korean=False):
    title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs = review_sections(flat, korean)
    deep = review_deep_dive(flat, korean)
    lang = "ko" if korean else "en"
    heading_refs = "선정 참고문헌 예시" if korean else "Selected References"
    heading_findings = "핵심 발견" if korean else "Key Findings"
    heading_category = "분야별 해석" if korean else "Category-Level Interpretation"
    heading_future = "향후 연구 의제" if korean else "Future Research Agenda"
    html_doc = f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Georgia, 'Noto Serif KR', serif; max-width: 920px; margin: 40px auto; padding: 0 22px; line-height: 1.72; color:#172033; }}
    h1 {{ line-height:1.15; }}
    h2 {{ margin-top: 34px; }}
    li {{ margin: 6px 0; }}
    .abstract {{ background:#f5f7fb; border-left:4px solid #0f766e; padding:14px 18px; }}
    table {{ width:100%; border-collapse:collapse; margin:16px 0; }}
    th,td {{ border-bottom:1px solid #d9dee8; padding:8px; vertical-align:top; text-align:left; }}
    th {{ background:#f4f6fa; }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <p><strong>Generated:</strong> {date.today().isoformat()} &middot; <strong>Dataset:</strong> {len(flat)} papers</p>
  <h2>Abstract</h2>
  <p class="abstract">{html.escape(abstract)}</p>
  <h2>1. Introduction and Scope</h2>
  <p>{html.escape(methods)}</p>
  <h2>2. {heading_findings}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['findings'])}</ul>
  <h2>3. Taxonomy</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in category_lines)}</ul>
  <h2>4. {heading_category}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['category_discussion'])}</ul>
  <h2>5. Year-by-Year Trends</h2>
  <p>{html.escape(trends_intro)}</p>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in year_lines)}</ul>
  <h2>6. {deep['top_cited_heading']}</h2>
  {html_ranked_table(deep['top_cited'], 'citations')}
  <h2>7. {deep['top_scored_heading']}</h2>
  {html_ranked_table(deep['top_scored'], 'importance')}
  <h2>8. {heading_future}</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in deep['future'])}</ul>
  <h2>9. Limitations</h2>
  <p>{html.escape(caveat)}</p>
  <h2>10. Conclusion</h2>
  <p>{html.escape(conclusion)}</p>
  <h2>{heading_refs}</h2>
  <ol>{''.join(f'<li>{html.escape(ref)}</li>' for ref in refs)}</ol>
</body>
</html>
"""
    name = "review_ko.html" if korean else "review_en.html"
    (PAPER_DIR / name).write_text(html_doc, encoding="utf-8")


def write_review_docx(flat):
    title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs = review_sections(flat, korean=False)
    deep = review_deep_dive(flat, korean=False)
    doc = Document()
    doc.add_heading(title, level=0)
    doc.add_paragraph(f"Generated: {date.today().isoformat()} | Dataset: {len(flat)} papers")
    doc.add_heading("Abstract", level=1)
    doc.add_paragraph(abstract)
    doc.add_heading("1. Introduction and Scope", level=1)
    doc.add_paragraph(methods)
    doc.add_heading("2. Key Findings", level=1)
    for line in deep["findings"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("3. Taxonomy", level=1)
    for line in category_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("4. Category-Level Interpretation", level=1)
    for line in deep["category_discussion"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("5. Year-by-Year Trends", level=1)
    doc.add_paragraph(trends_intro)
    for line in year_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("6. Top Papers by Citation Count", level=1)
    for p in deep["top_cited"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['citationCount']} citations)", style="List Number")
    doc.add_heading("7. Top Papers by Metadata Importance Score (Audit Signal)", level=1)
    for p in deep["top_scored"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['importanceScore']})", style="List Number")
    doc.add_heading("8. Future Research Agenda", level=1)
    for line in deep["future"]:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("9. Limitations", level=1)
    doc.add_paragraph(caveat)
    doc.add_heading("10. Conclusion", level=1)
    doc.add_paragraph(conclusion)
    doc.add_heading("Selected References", level=1)
    for ref in refs:
        doc.add_paragraph(ref, style="List Number")
    doc.save(PAPER_DIR / "review_en.docx")


def main():
    for path in (DATA_DIR, DOCS_DIR, PAPER_DIR):
        path.mkdir(exist_ok=True)
    selected, candidates = collect_papers()
    flat = write_json_csv(selected, candidates)
    write_taxonomy_dataset(flat)
    write_readme(flat)
    write_charts(flat)
    write_site(flat)
    write_review_html(flat, korean=False)
    write_review_html(flat, korean=True)
    write_review_docx(flat)
    shutil.copyfile(DATA_DIR / PAPERS_CSV, DOCS_DIR / "data" / PAPERS_CSV)
    shutil.copyfile(DATA_DIR / TAXONOMY_CSV, DOCS_DIR / "data" / TAXONOMY_CSV)
    shutil.copyfile(DATA_DIR / CANDIDATES_CSV, DOCS_DIR / "data" / CANDIDATES_CSV)
    shutil.copyfile(PAPER_DIR / "review_en.html", DOCS_DIR / "paper" / "review_en.html")
    shutil.copyfile(PAPER_DIR / "review_ko.html", DOCS_DIR / "paper" / "review_ko.html")
    (ROOT / "LICENSE").write_text("CC-BY-4.0 for text and metadata curation; upstream paper metadata belongs to original sources.\n", encoding="utf-8")
    print(f"[done] generated {len(flat)} selected papers", flush=True)


if __name__ == "__main__":
    main()
