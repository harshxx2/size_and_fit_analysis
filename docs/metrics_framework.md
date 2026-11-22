# Metrics Framework

We adopt the **HEART** framework (Happiness, Engagement, Adoption, Retention, Task Success) to track the impact of the Size Recommendation Experience.

## North Star Metric
- **Fit‑related Return Rate Reduction** – Percentage decrease in non‑fit feedback (small + large) on PDPs relative to baseline (26.22 %). Target: **≥ 4 pp** reduction after 4 weeks.

## Metric Hierarchy
| Dimension | Metric | Type | Target | Data Source |
|---|---|---|---|---|
| **Happiness** | Average post‑interaction rating (1‑10) | Survey (in‑app) | ≥ 8.5 | Feedback API |
| **Engagement** | Recommendation Card View Rate | Event count / Pageview | ≥ 30 % | Analytics SDK |
| **Adoption** | Recommendation Click‑Through Rate (CTR) | Clicks / Card Views | ≥ 15 % | Analytics SDK |
| **Retention** | Repeat Purchase of Same Category (30‑day) | Users with ≥2 orders | No dip > 2 % | Order DB |
| **Task Success** | Size Recommendation Accuracy | (Correct suggestion) / (Total suggestions) | ≥ 70 % | Offline evaluation against `fit_feedback.db` |

## Guardrails (Negative Impacts)
- **Add‑to‑Bag Conversion Rate** – Must not drop more than **2 %** (baseline measured before launch).
- **Page Load Time (p95)** – Must stay **< 120 ms** for the recommendation component.
- **Error Rate** – API error responses < **1 %** of recommendation calls.

## Reporting Cadence
- **Daily** – Dashboard metrics (Engagement, Adoption, Guardrails) refreshed via Tableau extract.
- **Weekly** – North Star trend, accuracy validation, and anomaly alerts.
- **Post‑Experiment** – Full statistical analysis of hypothesis outcome.

---
*All metric formulas reference the processed SQLite database (`fit_feedback.db`) and the analytics event logs generated during the pilot.*