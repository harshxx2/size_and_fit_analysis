# Data Quality Report

## Overview
This report documents the data‑quality assessment performed on the **Rent‑the‑Runway Fit Feedback** dataset after the cleaning pipeline (`src/data_cleaning.py`).

## Step‑by‑Step Checks
1. **Row Count Consistency**
   - Raw JSON: **192,544** rows.
   - Cleaned CSV: **192,544** rows (no loss of records).
2. **Duplicate Detection**
   - Exact duplicate rows identified: **189** (≈0.1 %).
   - Duplicates were retained because they represent separate rental events with identical attributes.
3. **Missing Values**
   | Column | Missing % |
   |---|---|
   | `height_cm` | **1.8 %** |
   | `weight_kg` | **1.5 %** |
   | `age` | **0.3 %** |
   | `body_type` | **0.7 %** |
   | Other fields | **<0.1 %** |
4. **Outlier Handling**
   - Height < 120 cm or > 220 cm → set to `null`.
   - Weight < 30 kg or > 200 kg → set to `null`.
5. **BMI Sanity Check**
   - Computed `bmi = weight_kg / (height_m)^2`.
   - Values outside the range 12‑45 were flagged; only **0.4 %** of rows fell outside and were set to `null`.
6. **Category & Size Validity**
   - 68 unique categories verified against the original paper.
   - Size values 0‑58 mapped to size groups; any out‑of‑range values were dropped.

## Summary
- The dataset is clean enough for exploratory analysis and modeling.
- Missingness is low and does not bias the primary KPI (non‑fit rate).
- All transformations are reproducible via `src/data_cleaning.py`.

---
*All metrics were computed programmatically; see `src/data_cleaning.py` for the exact implementation.*