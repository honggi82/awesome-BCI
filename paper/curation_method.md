# Codex-Assisted Curation Method

This repository was prepared with a Codex-assisted workflow and free public
metadata sources.

## Scope

- Topic: Brain-Computer Interface (BCI) research.
- Years: 2000-2026.
- Candidate pool: up to 500 BCI-related candidate papers per year.
- Final list: 100 selected papers per year.
- Metadata source: Semantic Scholar Academic Graph paper search.

## Selection Protocol

1. Query BCI-related terms for each target year.
2. Filter records to the target publication year.
3. Keep records whose title directly matches BCI terminology, or whose abstract
   has multiple BCI relevance signals.
4. Deduplicate by DOI, arXiv ID, PubMed ID, CorpusId, or Semantic Scholar paperId.
5. Score candidates with a transparent importance score:
   - log-scaled citation count
   - log-scaled influential citation count
   - recognized venue signals
   - BCI relevance-term density
   - bonuses for reviews/surveys, datasets/benchmarks, clinical or
     rehabilitation relevance, invasive/high-bandwidth interfaces, and modern
     machine-learning methods
6. Keep the top 500 scored candidates per year as the audited candidate pool.
7. Select the top 100 per year for the awesome list by citation count, using
   influential citation count and the metadata importance score as tie-breakers.

## Cost and API Boundary

The generated artifacts use free public metadata and local file generation.
No paid API call is required for reproducing the dataset and static site.

## Reproducibility

Run:

```bat
cd /d E:\조선대\연구\awesome-BCI
set PYTHONUTF8=1
python scripts\build_awesome_bci.py
```

The script regenerates:

- `README.md`
- `docs/index.html`
- `data/papers_2000_2026.csv`
- `data/candidates_top500_2000_2026.csv`
- `paper/review_en.docx`
- `paper/review_en.html`
- `paper/review_ko.html`
