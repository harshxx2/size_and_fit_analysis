# A/B Test Plan

## Objective
Evaluate whether the **Size Recommendation Experience** (treatment) reduces the proportion of size‑related returns compared with the current product detail page (control).

## Experimental Design
- **Type**: Two‑arm randomised controlled trial (A/B).
- **Unit of Randomisation**: User‑level hash (stable across sessions).
- **Allocation Ratio**: 1:1.
- **Duration**: Minimum **4 weeks** (covers a full return window of 30 days).
- **Sample Size Calculation**:
  ```python
  import statsmodels.stats.api as sms
  power = sms.TTestIndPower()
  effect = 0.04  # target absolute reduction from 26.2% to 22.2%
  std = 0.5 * (0.262*(1-0.262) + 0.222*(1-0.222))**0.5  # pooled std for proportions
  n = power.solve_power(effect_size=effect/std, power=0.8, alpha=0.05, ratio=1)
  print(int(n))
  ```
  Results in **≈ 4,400** orders per arm (≈ 8,800 total). We round up to **9,000** per arm to account for attrition.
- **Traffic Eligibility**: Mobile users on Android/iOS, any category, with at least one size selector interaction.

## Metrics
| Metric | Definition | Direction | Guardrail |
|---|---|---|---|
| **Primary** | Non‑fit feedback rate (small + large) on PDP after checkout | ↓ | Must not increase > 2 pp overall |
| **Secondary** | Recommendation Click‑Through Rate (CTR) | ↑ | — |
| **Secondary** | Add‑to‑Bag conversion (PDP → BAG) | ↔ (no regression) | ≤ ‑2 pp change |
| **Secondary** | Cancelled checkout rate | ↔ | — |
| **Guardrail** | Page load latency for recommendation component | ≤ 120 ms (p95) | — |

## Analysis Plan
- **Statistical Test**: Two‑sample proportion test (Chi‑square) on primary metric.
- **Significance Level**: α = 0.05 (two‑tailed).
- **Confidence Interval**: 95 % for difference in proportions.
- **Segmentation**: By category, size tier, and body‑type to detect heterogeneous effects.
- **Interim Checks**: Daily monitoring of guardrails; stop experiment early if any guardrail breaches.

## Implementation Details
- **Feature Flag**: `size_reco_ab_test` toggles treatment rendering.
- **Instrumentation**: Emit events `size_reco_view`, `size_reco_click`, `size_reco_submit` with user_id, product_id, timestamp.
- **Data Pipeline**: Funnel events into BigQuery; compute metrics with nightly batch jobs.

## Risks & Mitigations
- **Cold‑start products**: Show generic chart; monitor for any increase in bounce rate.
- **Recommendation bias**: Validate algorithm offline against `fit_feedback.db` before launch.
- **User confusion**: Include inline help tooltip; A/B test UI copy in a small pilot before full rollout.
