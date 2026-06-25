import csv
import html
import json
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
    text = " ".join([paper.get("title") or "", paper.get("abstract") or ""])
    return any(re.search(pattern, text, re.I) for pattern in RELEVANCE_PATTERNS)


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
                int(p.get("citationCount") or 0),
                int(p.get("influentialCitationCount") or 0),
                p.get("title") or "",
            ),
            reverse=True,
        )
        all_candidates[year] = [normalize_paper(p, year, i + 1, candidate=True) for i, p in enumerate(ranked)]
        selected[year] = [normalize_paper(p, year, i + 1) for i, p in enumerate(ranked[:TARGET_PER_YEAR])]
        print(f"[collect] {year}: {len(selected[year])}/{TARGET_PER_YEAR} selected from {len(ranked)} candidates", flush=True)
    return selected, all_candidates


def normalize_paper(paper, year, rank, candidate=False):
    ext = paper.get("externalIds") or {}
    oa = paper.get("openAccessPdf") or {}
    fields = paper.get("s2FieldsOfStudy") or []
    return {
        "year": year,
        "rank": rank,
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
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / "papers_2020_2026.json").open("w", encoding="utf-8") as f:
        json.dump({"generated": date.today().isoformat(), "target_per_year": TARGET_PER_YEAR, "papers": flat}, f, ensure_ascii=False, indent=2)
    with (DATA_DIR / "candidates_2020_2026.json").open("w", encoding="utf-8") as f:
        json.dump({"generated": date.today().isoformat(), "candidates": candidates}, f, ensure_ascii=False, indent=2)
    fields = list(flat[0].keys()) if flat else []
    with (DATA_DIR / "papers_2020_2026.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(flat)
    for year in YEARS:
        rows = selected.get(year, [])
        with (DATA_DIR / f"papers_{year}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
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
        f"Generated on {date.today().isoformat()} from free public Semantic Scholar metadata. The current edition selects up to {TARGET_PER_YEAR} BCI-related papers per year for 2020-2026.",
        "",
        "## Project Links",
        "",
        "- Website: `docs/index.html`",
        "- Full dataset: `data/papers_2020_2026.csv`",
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
            "| Rank | Paper | Venue | Citations | Category |",
            "| --- | --- | --- | ---: | --- |",
        ])
        for p in rows:
            lines.append(
                f"| {p['rank']} | {md_link(p['title'], p['url'])} | {p['venue'] or '-'} | "
                f"{p['citationCount']} | {p['category']} |"
            )
        lines.extend(["", "</details>", ""])
    lines.extend([
        "## Method",
        "",
        "The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and ranked by citation count with influential citations retained as metadata.",
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
        "<thead><tr><th>Rank</th><th>Paper</th><th>Venue</th><th>Citations</th><th>Category</th></tr></thead>",
        "<tbody>",
    ]
    for p in rows[:limit] if limit else rows:
        title = html.escape(p["title"])
        url = html.escape(p["url"])
        link = f'<a href="{url}">{title}</a>' if url else title
        out.append(
            f"<tr><td>{p['rank']}</td><td>{link}<br><small>{html.escape(p['authors'])}</small></td>"
            f"<td>{html.escape(p['venue'] or '-')}</td><td>{p['citationCount']}</td>"
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
    <p>A citation-ranked, year-by-year map of Brain-Computer Interface research from 2020 through 2026.</p>
    <nav>
      <a href="https://github.com/honggi82/awesome-BCI">README</a>
      <a href="data/papers_2020_2026.csv">CSV Dataset</a>
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
            "연도별 최대 100편씩 수집해 정리한다. 선별은 무료 공개 Semantic Scholar 메타데이터를 "
            "사용했으며, 검색어 기반 후보군을 연도 필터, BCI 관련성 필터, 중복 제거, 인용 수 정렬로 처리했다. "
            "결과는 운동상상/운동 디코딩, SSVEP/P300/ERP, 재활과 신경보철, 침습형 인터페이스, 딥러닝, EEG 신호처리, "
            "언어/의사소통 BCI, 폐루프/하이브리드 BCI로 나뉜다."
        )
        methods = (
            "방법: 각 연도에 대해 BCI 관련 질의를 Semantic Scholar Academic Graph bulk search에 보내고, "
            "제목 또는 초록에 BCI 관련 핵심 표현이 있는 논문만 남겼다. DOI, arXiv, PubMed, CorpusId, paperId 순서로 "
            "중복을 제거하고 citationCount 내림차순으로 정렬했다. 2026년은 2026-06-25 현재의 부분 연도라는 점에 유의해야 한다."
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
            "This draft review maps Brain-Computer Interface (BCI) research from 2020 through 2026, selecting up to "
            "100 papers per year from free public Semantic Scholar metadata. Candidate papers were retrieved with BCI-related "
            "queries, filtered by target year and relevance terms, deduplicated, and ranked by citation count. The resulting "
            "collection highlights work on motor imagery and movement decoding, SSVEP/P300/ERP systems, rehabilitation and "
            "neuroprosthetics, invasive interfaces, deep learning, EEG signal processing, speech and communication BCIs, and "
            "hybrid or closed-loop systems."
        )
        methods = (
            "Methods: For each year, BCI-oriented queries were sent to the Semantic Scholar Academic Graph bulk search endpoint. "
            "Records were retained when their title or abstract matched BCI relevance expressions, deduplicated by DOI, arXiv, "
            "PubMed, CorpusId, or paperId, and sorted by citationCount. The year 2026 should be interpreted as a partial year as of 2026-06-25."
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


def write_review_html(flat, korean=False):
    title, abstract, methods, trends_intro, category_lines, year_lines, caveat, conclusion, refs = review_sections(flat, korean)
    lang = "ko" if korean else "en"
    heading_refs = "선정 참고문헌 예시" if korean else "Selected References"
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
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <p><strong>Generated:</strong> {date.today().isoformat()} &middot; <strong>Dataset:</strong> {len(flat)} papers</p>
  <h2>Abstract</h2>
  <p class="abstract">{html.escape(abstract)}</p>
  <h2>1. Introduction and Scope</h2>
  <p>{html.escape(methods)}</p>
  <h2>2. Taxonomy</h2>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in category_lines)}</ul>
  <h2>3. Year-by-Year Trends</h2>
  <p>{html.escape(trends_intro)}</p>
  <ul>{''.join(f'<li>{html.escape(x)}</li>' for x in year_lines)}</ul>
  <h2>4. Limitations</h2>
  <p>{html.escape(caveat)}</p>
  <h2>5. Conclusion</h2>
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
    doc = Document()
    doc.add_heading(title, level=0)
    doc.add_paragraph(f"Generated: {date.today().isoformat()} | Dataset: {len(flat)} papers")
    doc.add_heading("Abstract", level=1)
    doc.add_paragraph(abstract)
    doc.add_heading("1. Introduction and Scope", level=1)
    doc.add_paragraph(methods)
    doc.add_heading("2. Taxonomy", level=1)
    for line in category_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("3. Year-by-Year Trends", level=1)
    doc.add_paragraph(trends_intro)
    for line in year_lines:
        doc.add_paragraph(line, style="List Bullet")
    doc.add_heading("4. Limitations", level=1)
    doc.add_paragraph(caveat)
    doc.add_heading("5. Conclusion", level=1)
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
    shutil.copyfile(PAPER_DIR / "review_en.html", DOCS_DIR / "paper" / "review_en.html")
    shutil.copyfile(PAPER_DIR / "review_ko.html", DOCS_DIR / "paper" / "review_ko.html")
    (ROOT / "LICENSE").write_text("CC-BY-4.0 for text and metadata curation; upstream paper metadata belongs to original sources.\n", encoding="utf-8")
    print(f"[done] generated {len(flat)} selected papers", flush=True)


if __name__ == "__main__":
    main()
