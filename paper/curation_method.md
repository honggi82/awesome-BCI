# Awesome BCI Curation Method

Generated: 2026-06-26

## Scope

- Topic: Brain-Computer Interface (BCI) research.
- Years: 2000-2026.
- Candidate pool: up to 500 BCI-related candidate papers per year.
- Final list: top 100 selected papers per year where available.
- Metadata source: Semantic Scholar Academic Graph paper search.

## Selection Protocol

- Query BCI-related terms for each target year.
- Filter records to the target publication year.
- Keep records whose title directly matches BCI terminology, or whose abstract has multiple BCI relevance signals.
- Deduplicate by DOI, arXiv ID, PubMed ID, CorpusId, Semantic Scholar paperId, or normalized title.
- Keep the top 500 scored candidates per year as the audited candidate pool.
- Select the top 100 per year for the awesome list by citation count, using influential citation count and metadata importance score as tie-breakers.

## GitHub-Awesome Skill2 and Paper-Curation Provenance

This regeneration follows `github-awesome-skill2` in metadata-adapter mode for a large citation-ranked awesome repository while preserving the selected paper set in `data/papers_2000_2026.csv`. The workflow inspected the local `jehyunlee/paper-curation` checkout and is configured for Zotero-free folder-source PDF staging under `E:\조선대\연구\paper-curation\paper\awesome-BCI`. Full PDF LLM review stages from paper-curation were not run because they require explicit approval for paid or metered APIs.

## Cost and API Boundary

The generated artifacts use free public metadata and local file generation. No paid API call is required for reproducing the dataset and static site.

## Reproducibility

Run `PYTHONUTF8=1 python scripts\build_awesome_bci.py` from the repository root to regenerate the README, data files, static site, review drafts, and this curation method.
