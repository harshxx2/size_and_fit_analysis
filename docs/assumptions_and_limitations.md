# Assumptions and Limitations

## Data‑Source Assumptions
- The **Rent‑the‑Runway Fit Feedback** dataset is used as a proxy for Indian e‑commerce sizing problems. It is sourced from the UCSD RecSys 2018 paper (Misra et al.) and released under a **CC‑BY‑4.0** license.
- All user‑identifiers are anonymised; any demographic analysis assumes the sample is representative of a broader online shopper population.
- Height and weight strings are free‑text; parsing heuristics may mis‑interpret unconventional formats (e.g., "5ft10in"). Those rows are set to null.
- The `size` field is a numeric label from 0‑58, which we map to size groups (XS‑XXXL+) based on typical US sizing, not Indian size charts.

## Analytical Limitations
- **Rental vs Purchase**: The dataset reflects rental experiences; purchase behaviour, return logistics, and price sensitivity differ for Myntra shoppers.
- **Cultural Fit Preferences**: Indian fashion silhouettes and cultural fit expectations (e.g., loose versus fitted) are not captured.
- **Missing Variables**: No data on fabric stretch, brand sizing conventions, or user measurement devices (e.g., tape vs app).
- **Cold‑Start Items**: For items with fewer than 30 feedback entries we fall back to a generic chart; this threshold is arbitrary.
- **Temporal Relevance**: Data collected (2016‑2018) may not reflect current style trends or sizing standards.

## Modeling Assumptions
- The `fit_numeric` encoding treats both *small* and *large* as a failure equally; a more nuanced model could differentiate over‑ vs under‑sizing.
- BMI is computed from parsed height/weight and used only for exploratory segmentation; it is not a causal factor in the analysis.
- Recommendations are derived from majority vote in the historical feedback; no machine‑learning model is trained.

## Operational Constraints
- All analyses are performed offline on the cleaned CSV and SQLite DB. Real‑time recommendation serving is out of scope.
- The Tableau dashboard uses pre‑aggregated CSVs; live connections to the DB are not configured.
- Prototype screens are documented as markdown specifications; actual Figma files are not generated due to lack of a graphical editor.

---
*These assumptions and limitations should be disclosed during any interview discussion to demonstrate rigorous product thinking.*