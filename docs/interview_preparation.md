# Interview Preparation

## 60‑Second Elevator Pitch
"I built a data‑driven product case study for a fashion e‑commerce sizing recommendation feature. Using the public Rent‑the‑Runway fit‑feedback dataset (≈192k records), I cleaned and analysed patterns of size mismatches, derived a set of actionable product hypotheses, authored a full PRD and A/B test plan, and delivered a Tableau dashboard and UI wireframes. This demonstrates my ability to translate raw data into concrete product decisions, metrics, and prototype specifications—key skills for a PM intern at Myntra."

## 2‑Minute Walkthrough Outline
1. **Problem** – High return rates due to size/fit mismatches (30‑40 % in Indian e‑commerce).<br/>2. **Data** – Rental‑fashion dataset as a proxy; key KPI: non‑fit feedback rate (26.22 %).<br/>3. **Insights** – Category and size‑tier hotspots, body‑type effects, rating drop on mismatches.
4. **Solution** – Size recommendation card, heatmap, modal UI (wireframes attached).
5. **Metrics** – HEART framework; North Star: fit‑related return reduction ≥ 4 pp.
6. **Experiment** – A/B test design, sample size ~9k per arm, guardrails.
7. **Delivery** – Python pipeline, SQLite DB, Tableau dashboard, prototype specs, case study.

## Top 10 PM Interview Questions (with concise answers)
| Question | Answer (data‑backed) |
|---|---|
| 1. Why use a rental dataset for an Indian marketplace? | It provides a large, labeled fit‑feedback signal under a permissive CC‑BY‑4.0 license. While not identical, the patterns (size‑tier risk, body‑type effects) are transferable and clearly articulated in the **Assumptions** section. |
| 2. How do you handle cold‑start items? | Use a fallback generic size chart for items with < 30 feedback entries; the PRD specifies this rule (FR‑006). |
| 3. What metric would you monitor first after launch? | The **Non‑Fit Rate** on the PDP (primary KPI) plus **Recommendation CTR** (adoption). |
| 4. How do you ensure the recommendation does not hurt conversion? | Guardrail **Add‑to‑Bag** change ≤ ‑2 pp; monitor daily and abort if breach. |
| 5. Explain the sample size calculation. | Using `statsmodels.stats.power.TTestIndPower`, we target a 4 pp absolute reduction (effect size) with α=0.05, power=0.8, yielding ~4,400 orders per arm; rounded to 9k per arm for attrition. |
| 6. What biases might affect your analysis? | Rental‑vs‑purchase behavior, US sizing conventions, missing measurements, limited demographic diversity – all listed in **Assumptions and Limitations**. |
| 7. How would you improve the model? | Incorporate brand‑specific sizing, fabric stretch, and user‑provided measurements; train a supervised classifier on `fit_numeric`. |
| 8. How do you prioritize features in the PRD? | Impact vs effort matrix; sizing recommendation (high impact, medium effort) prioritized over secondary personalization. |
| 9. Describe a failure you encountered and fixed. | Height parsing mis‑interpreted strings like "5ft10"; added regex fallback and logged affected rows, reducing height‑null rate from 5 % to < 1 %. |
| 10. How would you present this work to stakeholders? | One‑page executive summary (README), interactive Tableau dashboard, prototype mockups, and a concise case‑study PDF. |

---
Use these talking points to demonstrate analytical rigor, product thinking, and execution capability.
