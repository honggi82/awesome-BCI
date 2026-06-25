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
YEARS = list(range(2020, 2027))
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
        title_relevant = [p for p in candidate_pool if title_relevance_count(p) > 0]
        fill = [p for p in candidate_pool if title_relevance_count(p) == 0]
        selected_pool = (title_relevant + fill)[:TARGET_PER_YEAR]
        all_candidates[year] = [normalize_paper(p, year, i + 1, candidate=True) for i, p in enumerate(candidate_pool)]
        selected[year] = [normalize_paper(p, year, i + 1) for i, p in enumerate(selected_pool)]
        print(
            f"[collect] {year}: selected {len(selected[year])}/{TARGET_PER_YEAR} "
            f"from top {len(candidate_pool)}/{min(CANDIDATES_PER_YEAR, len(ranked))} candidates "
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
    with (DATA_DIR / "papers_2020_2026.json").open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "target_per_year": TARGET_PER_YEAR,
            "papers": flat,
        }, f, ensure_ascii=False, indent=2)
    with (DATA_DIR / "candidates_top500_2020_2026.json").open("w", encoding="utf-8") as f:
        json.dump({
            "generated": date.today().isoformat(),
            "candidate_pool_per_year": CANDIDATES_PER_YEAR,
            "candidates": candidate_flat,
        }, f, ensure_ascii=False, indent=2)
    fields = list(flat[0].keys()) if flat else []
    candidate_fields = list(candidate_flat[0].keys()) if candidate_flat else fields
    with (DATA_DIR / "papers_2020_2026.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flat)
    with (DATA_DIR / "candidates_top500_2020_2026.csv").open("w", encoding="utf-8-sig", newline="") as f:
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


def write_readme(flat):
    stats = year_stats(flat)
    cats = category_stats(flat)
    lines = [
        "# Awesome BCI",
        "",
        "[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)",
        "",
        "A curated, citation-ranked map of recent Brain-Computer Interface (BCI) research.",
        "",
        f"Generated on {date.today().isoformat()} from free public Semantic Scholar metadata. The current edition investigates up to {CANDIDATES_PER_YEAR} BCI-related candidate papers per year for 2020-2026, scores their importance, and selects the top {TARGET_PER_YEAR} papers per year.",
        "",
        "## Project Links",
        "",
        "- Website: `docs/index.html`",
        "- Selected dataset: `data/papers_2020_2026.csv`",
        "- Candidate pool: `data/candidates_top500_2020_2026.csv`",
        "- English review draft: `paper/review_en.html`, `paper/review_en.docx`",
        "- Korean review draft: `paper/review_ko.html`",
        "",
        "## Taxonomy",
        "",
    ]
    for cat, count in cats.most_common():
        lines.append(f"- **{cat}**: {count} papers")
    lines.extend(["", "## Yearly Collections", ""])
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    for year in YEARS:
        rows = by_year.get(year, [])
        top = rows[0]["title"] if rows else "n/a"
        lines.extend([
            f"### {year}",
            "",
            f"- Papers selected: **{len(rows)}**",
            f"- Total citations in selected set: **{stats.get(year, {}).get('citations', 0):,}**",
            f"- Top cited paper: **{top}**",
            "",
            "<details>",
            f"<summary>Show {year} papers</summary>",
            "",
            "| Rank | Paper | Venue | Importance | Citations | Category |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ])
        for p in rows:
            lines.append(
                f"| {p['rank']} | {md_link(p['title'], p['url'])} | {p['venue'] or '-'} | "
                f"{p['importanceScore']} | {p['citationCount']} | {p['category']} |"
            )
        lines.extend(["", "</details>", ""])
    lines.extend([
        "## Method",
        "",
        "The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and reduced to a maximum of 500 candidates per year. Importance scoring combines log-scaled citation count, log-scaled influential citation count, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive/high-bandwidth interfaces, and modern ML methods. The final awesome list uses the top 100 scored papers per year.",
        "",
        "## Caveats",
        "",
        "- Citation counts favor older papers and may under-rank recent 2026 work.",
        "- Metadata search is not equivalent to a full systematic review of PDFs.",
        "- Some venues and publication dates are missing in upstream metadata.",
    ])
    (ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def html_table(rows, limit=None):
    out = [
        "<table>",
        "<thead><tr><th>Rank</th><th>Paper</th><th>Venue</th><th>Importance</th><th>Citations</th><th>Category</th></tr></thead>",
        "<tbody>",
    ]
    for p in rows[:limit] if limit else rows:
        title = html.escape(p["title"])
        url = html.escape(p["url"])
        link = f'<a href="{url}">{title}</a>' if url else title
        out.append(
            f"<tr><td>{p['rank']}</td><td>{link}<br><small>{html.escape(p['authors'])}</small></td>"
            f"<td>{html.escape(p['venue'] or '-')}</td><td>{p['importanceScore']}</td><td>{p['citationCount']}</td>"
            f"<td>{html.escape(p['category'])}</td></tr>"
        )
    out.extend(["</tbody>", "</table>"])
    return "\n".join(out)


def write_site(flat):
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "assets").mkdir(exist_ok=True)
    (DOCS_DIR / "data").mkdir(exist_ok=True)
    (DOCS_DIR / "paper").mkdir(exist_ok=True)
    by_year = defaultdict(list)
    for p in flat:
        by_year[p["year"]].append(p)
    cats = category_stats(flat)
    total_cites = sum(p["citationCount"] for p in flat)
    sections = []
    for year in YEARS:
        rows = by_year.get(year, [])
        sections.append(f"<section><h2>{year}</h2>{html_table(rows)}</section>")
    cat_cards = "\n".join(
        f"<div class='card'><strong>{html.escape(cat)}</strong><span>{count} papers</span></div>"
        for cat, count in cats.most_common()
    )
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome BCI</title>
  <style>
    :root {{ color-scheme: light; --ink:#18212f; --muted:#5b6678; --line:#d9dee8; --accent:#0f766e; --accent2:#7c3aed; --bg:#f7f9fc; }}
    body {{ margin:0; font-family: Inter, Segoe UI, Arial, sans-serif; color:var(--ink); background:var(--bg); }}
    header {{ padding:56px 7vw 36px; background:linear-gradient(120deg,#e9fbf8,#eef2ff); border-bottom:1px solid var(--line); }}
    h1 {{ font-size:48px; margin:0 0 12px; letter-spacing:0; }}
    p {{ line-height:1.65; color:var(--muted); }}
    main {{ padding:28px 7vw 72px; }}
    .stats, .cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; margin:24px 0; }}
    .figures {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; margin:24px 0; }}
    .figures img {{ width:100%; background:white; border:1px solid var(--line); border-radius:8px; }}
    .stat, .card {{ background:white; border:1px solid var(--line); border-radius:8px; padding:16px; }}
    .stat strong {{ display:block; font-size:28px; color:var(--accent); }}
    .card span {{ display:block; margin-top:8px; color:var(--muted); }}
    nav a {{ display:inline-block; margin:0 12px 10px 0; color:var(--accent2); font-weight:600; }}
    section {{ margin-top:34px; }}
    table {{ width:100%; border-collapse:collapse; background:white; border:1px solid var(--line); border-radius:8px; overflow:hidden; }}
    th,td {{ padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top; text-align:left; }}
    th {{ background:#f0f4f8; }}
    small {{ color:var(--muted); }}
    a {{ color:#0f5f97; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
  </style>
</head>
<body>
  <header>
    <h1>Awesome BCI</h1>
    <p>A metadata-scored, year-by-year map of Brain-Computer Interface research from 2020 through 2026. Each year investigates up to {CANDIDATES_PER_YEAR} candidate papers and selects the top {TARGET_PER_YEAR}.</p>
    <nav>
      <a href="https://github.com/honggi82/awesome-BCI">README</a>
      <a href="data/papers_2020_2026.csv">CSV Dataset</a>
      <a href="data/candidates_top500_2020_2026.csv">Candidate Pool</a>
      <a href="paper/review_en.html">Review Paper</a>
      <a href="paper/review_ko.html">Korean Review</a>
    </nav>
  </header>
  <main>
    <div class="stats">
      <div class="stat"><strong>{len(flat)}</strong><span>selected papers</span></div>
      <div class="stat"><strong>{len(YEARS)}</strong><span>years covered</span></div>
      <div class="stat"><strong>{total_cites:,}</strong><span>citation count total</span></div>
      <div class="stat"><strong>{len(cats)}</strong><span>topic categories</span></div>
    </div>
    <h2>Taxonomy</h2>
    <div class="figures">
      <img src="assets/category_distribution.png" alt="Category distribution chart">
      <img src="assets/yearly_citations.png" alt="Yearly citation chart">
    </div>
    <div class="cards">{cat_cards}</div>
    {''.join(sections)}
  </main>
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
    ax.set_title("BCI Paper Taxonomy, 2020-2026")
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
        title = "2020-2026년 뇌-컴퓨터 인터페이스 연구 동향: 공개 메타데이터 기반 리뷰"
        abstract = (
            "이 리뷰 초안은 2020년부터 2026년까지의 Brain-Computer Interface(BCI) 연구를 "
            f"연도별 최대 {CANDIDATES_PER_YEAR}편의 후보로 조사하고 중요도 평가를 통해 {TARGET_PER_YEAR}편씩 선별해 정리한다. 선별은 무료 공개 Semantic Scholar 메타데이터를 "
            "사용했으며, 검색어 기반 후보군을 연도 필터, 강화된 BCI 관련성 필터, 중복 제거, 중요도 점수화로 처리했다. "
            "결과는 운동상상/운동 디코딩, SSVEP/P300/ERP, 재활과 신경보철, 침습형 인터페이스, 딥러닝, EEG 신호처리, "
            "언어/의사소통 BCI, 폐루프/하이브리드 BCI로 나뉜다."
        )
        methods = (
            "방법: 각 연도에 대해 BCI 관련 질의를 Semantic Scholar Academic Graph bulk search에 보내고, "
            "제목 또는 초록에 BCI 관련 핵심 표현이 있는 논문만 남겼다. DOI, arXiv, PubMed, CorpusId, paperId 순서로 "
            f"중복을 제거했다. 이후 연도별 최대 {CANDIDATES_PER_YEAR}편의 후보를 중요도 점수로 평가하고 상위 {TARGET_PER_YEAR}편을 최종 목록에 사용했다. "
            "중요도 점수는 로그 변환 인용 수, 영향력 있는 인용 수, 주요 venue 신호, BCI 핵심어 밀도, 리뷰/서베이, 데이터셋/벤치마크, "
            "임상/재활 관련성, 침습형 고대역폭 BCI, 최신 머신러닝 방법 보너스를 합산했다. 2026년은 2026-06-25 현재의 부분 연도라는 점에 유의해야 한다."
        )
        trends_intro = "주요 경향은 다음과 같다."
        caveat = (
            "한계: 이 문서는 전문 PDF를 모두 읽은 체계적 문헌고찰이 아니라 메타데이터 기반 리뷰 초안이다. "
            "인용 수는 최신 논문에 불리하며, 일부 논문의 venue/date 정보는 원천 데이터에서 누락될 수 있다."
        )
        conclusion = (
            "결론적으로 2020년대 BCI 연구는 딥러닝 기반 EEG 디코딩과 벤치마크, 재활 응용, 침습형 고성능 디코딩, "
            "사용자 친화적 의사소통 시스템 사이에서 빠르게 확장되고 있다. 향후 리뷰에서는 실제 PDF 기반 품질 평가, "
            "임상 전환성, 데이터셋 재현성, 장기 안정성, 안전성과 윤리 문제를 함께 검토해야 한다."
        )
    else:
        title = "Brain-Computer Interface Research from 2020 to 2026: A Metadata-Driven Review"
        abstract = (
            "This draft review maps Brain-Computer Interface (BCI) research from 2020 through 2026, investigating up to "
            f"{CANDIDATES_PER_YEAR} candidate papers per year from free public Semantic Scholar metadata and selecting {TARGET_PER_YEAR} papers per year by importance score. Candidate papers were retrieved with BCI-related "
            "queries, filtered by target year and strengthened BCI relevance terms, deduplicated, and scored for importance. The resulting "
            "collection highlights work on motor imagery and movement decoding, SSVEP/P300/ERP systems, rehabilitation and "
            "neuroprosthetics, invasive interfaces, deep learning, EEG signal processing, speech and communication BCIs, and "
            "hybrid or closed-loop systems."
        )
        methods = (
            "Methods: For each year, BCI-oriented queries were sent to the Semantic Scholar Academic Graph bulk search endpoint. "
            "Records were retained when their title or abstract matched BCI relevance expressions, deduplicated by DOI, arXiv, "
            f"PubMed, CorpusId, or paperId, and reduced to at most {CANDIDATES_PER_YEAR} candidate papers per year. The final {TARGET_PER_YEAR} papers per year were selected by an importance score that combines log-scaled citations, log-scaled influential citations, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive high-bandwidth BCIs, and modern machine-learning methods. The year 2026 should be interpreted as a partial year as of 2026-06-25."
        )
        trends_intro = "The main metadata-level trends are as follows."
        caveat = (
            "Limitations: this is a metadata-driven review draft rather than a full systematic review of every PDF. Citation counts "
            "favor older work, recent 2026 papers are structurally under-counted, and some venues or publication dates are missing upstream."
        )
        conclusion = (
            "Overall, BCI research in the 2020s is expanding across deep-learning EEG decoding, benchmarks and datasets, rehabilitation, "
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
            f"가장 큰 축은 {leading_cat}({leading_count}편)으로, 2020년대 BCI 연구가 여전히 운동 의도 해석과 운동 기능 보조를 중심으로 조직되어 있음을 보여준다.",
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
        top_scored_heading = "중요도 점수 상위 논문"
        top_cited_heading = "인용 수 상위 논문"
    else:
        findings = [
            f"The {len(flat)} selected papers account for {total_cites:,} citations in the selected set, with the largest citation mass in {peak_year}.",
            f"The dominant category is {leading_cat} ({leading_count} papers), indicating that movement intention decoding and motor assistance remain the organizing center of 2020s BCI research.",
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
        top_scored_heading = "Top Papers by Importance Score"
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
  <h2>6. {deep['top_scored_heading']}</h2>
  {html_ranked_table(deep['top_scored'], 'importance')}
  <h2>7. {deep['top_cited_heading']}</h2>
  {html_ranked_table(deep['top_cited'], 'citations')}
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
    doc.add_heading("6. Top Papers by Importance Score", level=1)
    for p in deep["top_scored"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['importanceScore']})", style="List Number")
    doc.add_heading("7. Top Papers by Citation Count", level=1)
    for p in deep["top_cited"]:
        doc.add_paragraph(f"{p['year']} #{p['rank']}: {p['title']} ({p['citationCount']} citations)", style="List Number")
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
    write_readme(flat)
    write_charts(flat)
    write_site(flat)
    write_review_html(flat, korean=False)
    write_review_html(flat, korean=True)
    write_review_docx(flat)
    shutil.copyfile(DATA_DIR / "papers_2020_2026.csv", DOCS_DIR / "data" / "papers_2020_2026.csv")
    shutil.copyfile(DATA_DIR / "candidates_top500_2020_2026.csv", DOCS_DIR / "data" / "candidates_top500_2020_2026.csv")
    shutil.copyfile(PAPER_DIR / "review_en.html", DOCS_DIR / "paper" / "review_en.html")
    shutil.copyfile(PAPER_DIR / "review_ko.html", DOCS_DIR / "paper" / "review_ko.html")
    (ROOT / "LICENSE").write_text("CC-BY-4.0 for text and metadata curation; upstream paper metadata belongs to original sources.\n", encoding="utf-8")
    print(f"[done] generated {len(flat)} selected papers", flush=True)


if __name__ == "__main__":
    main()
