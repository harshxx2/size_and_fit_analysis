# Dashboard Metrics

The Tableau dashboard is built around five core visualizations, each exposing a key business metric derived from the cleaned fit‑feedback data.

| Sheet | Metric | Definition | Data Source |
|---|---|---|---|
| **Fit Breakdown** | Overall Fit Distribution | Percentage of feedback labeled `fit` vs `small`/`large`. | `dashboard_data.csv` – aggregated counts per `fit`.
| **Non‑Fit by Category** | Category Non‑Fit Rate | `non_fit_rate = (small+large) / total_feedback` per category (min 200 feedback rows). | `category_stats.csv`.
| **Sizing Risk by Size Tier** | Size Tier Non‑Fit Rate | Same calculation aggregated on `size_group`. | `size_stats.csv`.
| **Body‑Type Heatmap** | Fit Outcome by Body Type | Percentage of each `fit` outcome within each `body_type`. | `body_type_stats.csv`.
| **Category × Size Heatmap** | Cross‑Tab Non‑Fit Rate | Heatmap of `non_fit_rate` for each `(category, size_group)` pair. | `category_size_stats.csv`.

## KPI Mapping
- **North Star** – Reduction in overall non‑fit rate (primary KPI from Sheet 1).
- **Leading Metrics** – Adoption of recommendation (tracked via event pipeline, not in dashboard) and engagement with the size‑risk visualizations (filter usage).
- **Guardrails** – Add‑to‑Bag conversion and page‑load latency, monitored outside Tableau.

---
*All CSVs are pre‑aggregated by `src/analysis.py` and stored in the `dashboard/` folder.*