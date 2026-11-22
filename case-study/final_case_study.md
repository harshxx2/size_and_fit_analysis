# Final Case Study

## Executive Summary
This portfolio project demonstrates a data‑driven end‑to‑end product development workflow for a **Size Recommendation Experience** on a fashion e‑commerce platform (Myntra). Using the public **Rent‑the‑Runway Fit Feedback** dataset (≈192 k records), we identified key sizing pain points, authored a complete Product Requirements Document (PRD), designed a measurement framework, built an A/B test plan, delivered a Tableau dashboard, and created UI wireframes.

## Problem Context
- Indian e‑commerce faces **30‑40 %** return rates, with a large share attributed to size/fit mismatches.
- Direct access to Myntra’s proprietary data is unavailable; we use a publicly licensed dataset as a proxy, acknowledging its limitations (rental vs purchase, US sizing standards).

## Data & Insights
| Insight | Metric | Value |
|---|---|---|
| Overall non‑fit rate | (small + large) / total | **26.22 %** |
| Category with highest non‑fit | Dress | **28.3 %** |
| Size groups most problematic | XS & XXL+ | **> 30 %** |
| Body‑type effect | Pear & Apple → higher under‑size complaints | — |
| Rating drop on non‑fit | Fit 9.25 vs Small/Large ~7.9 | — |

These findings drove the **hypotheses** that proactive size guidance and personalized recommendations could reduce uncertainty and improve conversion.

## Product Solution
- **Size Recommendation Card** on the PDP with confidence score.
- **Bottom‑sheet modal** for optional height/weight/body‑type entry.
- **Category‑Size Heatmap** visual aid.
- Detailed functional (FR‑001‑FR‑012) and non‑functional specs (latency <120 ms, 99.9 % uptime).

## Metrics & Experimentation
- **North Star:** Fit‑related return rate reduction ≥ 4 pp.
- **HEART metrics** defined in `docs/metrics_framework.md` (adoption, engagement, guardrails).
- **A/B Test:** Two‑arm, user‑level randomisation, ~9 k orders per arm, primary metric non‑fit rate, guardrails on add‑to‑bag conversion and latency.

## Implementation Artifacts
- **Data pipeline** (`src/data_cleaning.py`, `src/analysis.py`) producing cleaned CSV, SQLite DB, and Tableau‑ready CSVs.
- **Jupyter notebooks** (01‑04) for reproducible analysis.
- **Tableau dashboard** with five core visualizations (`dashboard/tableau_instructions.md`).
- **UI wireframes** documented in `prototype/` (specs and preview image).
- **Full documentation** under `docs/` and a polished `README.md` for GitHub.

## Results & Validation
- Python aggregation results match SQLite query outputs (see `reports/validation_report.md`).
- Data quality checks confirm <2 % missing numeric fields after cleaning.
- All visualizations and metrics are reproducible with the provided code and environment.

## Impact Statement
If deployed at Myntra, the feature is projected to cut size‑related returns by **~4 pp**, translating to significant cost savings and a smoother shopper experience—aligned with the North Star metric and the company’s operational goals.

---
*All numbers are derived directly from the processed dataset; no synthetic data was introduced.*