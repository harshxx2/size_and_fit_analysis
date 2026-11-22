# Data Dictionary

This document describes each column in the processed dataset `renttherunway_cleaned.csv` and the derived SQLite table `fit_feedback`.

| Column | Type | Description | Source / Transformation |
|---|---|---|---|
| `user_id` | STRING | Anonymised identifier for the renter. | Raw `user_id` (hashed).
| `item_id` | STRING | Unique identifier for the apparel item. | Raw `item_id`.
| `category` | STRING | High‑level product category (e.g., *dress*, *pants*). | Raw `category` – normalized to lower case.
| `size` | STRING | Reported size label (numeric 0‑58). | Raw `size` – converted to integer, then bucketed into size groups (XS‑XXXL+).
| `size_group` | STRING | Size tier (XS, S, M, L, XL, XXL, XXXL+). | Derived from `size` ranges.
| `fit` | STRING | Fit outcome: `fit`, `small`, or `large`. | Raw `fit` – cleaned of whitespace.
| `height_cm` | FLOAT | Height in centimeters. | Parsed from free‑text height strings, converted to cm.
| `weight_kg` | FLOAT | Weight in kilograms. | Parsed from free‑text weight strings, converted to kg.
| `body_type` | STRING | Self‑reported silhouette (e.g., *hourglass*, *pear*). | Normalized to canonical set of 7 types.
| `age` | INTEGER | Age of the renter. | Raw `age` – cleaned, outliers (< 12 or > 100) set to null.
| `rating` | FLOAT | 1‑10 rating of overall satisfaction. | Raw `rating` – cast to float.
| `rented_for` | STRING | Intended use (e.g., *party*, *work*). | Kept as categorical string.
| `review_text` | STRING | Free‑text review. | Raw `review_text` – trimmed.
| `bmi` | FLOAT | Body Mass Index (weight_kg / (height_m)^2). | Computed from `height_cm` and `weight_kg`.
| `fit_numeric` | INTEGER | Numeric encoding of `fit` (1=fit, 0=small/large). | Derived for modeling.

All numeric columns are stored as REAL in SQLite; categorical columns as TEXT.

---
*The schema is also defined in `src/utils.py` for programmatic reference.*