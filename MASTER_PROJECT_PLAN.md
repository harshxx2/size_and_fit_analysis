# MASTER EXECUTION & HANDOVER PLAN: MYNTRA SIZE & FIT ANALYSIS
**Portfolio Project:** Size & Fit Analysis: PRD, Data Analysis, Dashboard & Prototype  
**Target Goal:** Product Manager Intern Application at Myntra  
**Status:** In Progress (Data Pipeline, EDA, SQLite DB, Charts, & Core SQL completed; Documentation, Notebooks, Dashboard & Prototype in progress)  
**Date of Record:** November 2026  

---

## 1. PROJECT OVERVIEW & CONTEXT

### Purpose
This independent portfolio project demonstrates how an aspiring Product Manager uses real fit-feedback data to:
1. Diagnose sizing and fit mismatch patterns in apparel e-commerce.
2. Formulate product hypotheses for an Indian fashion e-commerce context (Myntra mobile app).
3. Author an executive-grade Product Requirements Document (PRD) and A/B Testing Experiment Plan.
4. Provide production SQL queries, BI dashboard specs, interactive Jupyter notebooks, and mobile UI wireframes.

### Golden Rules & Ethical Guardrails (Crucial for Interviews)
1. **Source Transparency:** The underlying data is the **RentTheRunway Fit Feedback Dataset** (Misra et al., UCSD, CC BY 4.0, ~192.5k records). It is rental fashion data from the US, **not** proprietary Myntra transaction data.
2. **Metric Precision:** The dataset contains self-reported fit outcomes (`fit`, `small`, `large`). "Non-fit rate" is defined strictly as `(small + large) / total_valid_records * 100`. It serves as a **directional proxy** for sizing uncertainty and return risk, not an empirical return rate.
3. **No Bluffed A/B Testing:** The A/B test plan is a **proposed pre-launch experiment design**, complete with statistical power calculations and guardrails, not a concluded experiment.
4. **No Fabricated Numbers:** All figures in reports and summaries must match the exact outputs of `src/data_cleaning.py`, `src/analysis.py`, and `data/processed/fit_feedback.db`.

---

## 2. REPOSITORY ARCHITECTURE & CURRENT STATE

Project Root: `c:\Users\champ\Desktop\Myntra-size and fit analysis\myntra-size-fit-analysis\`

```
myntra-size-fit-analysis/
├── MASTER_PROJECT_PLAN.md                  <-- [THIS FILE: Complete handover & execution blueprint]
├── requirements.txt                        <-- [PENDING: Phase 5]
├── README.md                               <-- [PENDING: Phase 5]
├── data/
│   ├── README.md                           <-- [PENDING: Phase 2]
│   ├── raw/
│   │   ├── renttherunway_final_data.json   <-- [DONE: 192,544 records, 123 MB]
│   │   └── modcloth_final_data.json        <-- [DONE: Downloaded as part of package]
│   └── processed/
│       ├── renttherunway_cleaned.csv       <-- [DONE: Cleaned CSV, 97.5 MB, 35 columns]
│       ├── data_summary.json               <-- [DONE: Summary JSON metrics]
│       └── fit_feedback.db                 <-- [DONE: SQLite DB, 192,544 rows, indexed]
├── notebooks/
│   ├── 01_data_understanding.ipynb         <-- [PENDING: Phase 3]
│   ├── 02_data_cleaning.ipynb              <-- [PENDING: Phase 3]
│   ├── 03_exploratory_analysis.ipynb       <-- [PENDING: Phase 3]
│   └── 04_fit_insights.ipynb               <-- [PENDING: Phase 3]
├── src/
│   ├── __init__.py                         <-- [DONE]
│   ├── utils.py                            <-- [DONE: Reusable filters, aggregators, color palettes]
│   ├── data_cleaning.py                    <-- [DONE: Parsing, unit conversion, feature engineering]
│   └── analysis.py                         <-- [DONE: Matplotlib chart generation & aggregations]
├── sql/
│   ├── schema.sql                          <-- [DONE: DDL with 8 indexes]
│   ├── 01_category_analysis.sql            <-- [DONE: Volume, non-fit rates, benchmark comparisons]
│   ├── 02_size_analysis.sql                <-- [DONE: Sizing tiers, raw sizes, problem matrices]
│   ├── 03_body_type_analysis.sql           <-- [DONE: Silhouette cuts, BMI & measurement stats]
│   └── 04_fit_summary.sql                  <-- [DONE: Executive KPIs, rating correlation, ranking]
├── dashboard/
│   ├── dashboard_data.csv                  <-- [DONE: Full flat table for Tableau/PowerBI]
│   ├── category_stats.csv                  <-- [DONE: Pre-aggregated category table]
│   ├── size_stats.csv                      <-- [DONE: Pre-aggregated size tier table]
│   ├── body_type_stats.csv                 <-- [DONE: Pre-aggregated body type table]
│   ├── category_size_stats.csv             <-- [DONE: Heatmap cross-tab table]
│   ├── tableau_instructions.md             <-- [PENDING: Phase 4]
│   ├── dashboard_metrics.md                <-- [PENDING: Phase 4]
│   ├── dashboard_preview.png               <-- [PENDING: Phase 4 composite canvas]
│   └── charts/                             <-- [DONE: 10 high-res charts generated]
│       ├── chart_01_fit_distribution.png
│       ├── chart_02_nonfit_by_category.png
│       ├── chart_03_nonfit_by_size.png
│       ├── chart_04_body_type.png
│       ├── chart_05_category_size_heatmap.png
│       ├── chart_06_rating_vs_fit.png
│       ├── chart_07_rental_purpose.png
│       ├── chart_08_age_group.png
│       ├── chart_09_height_weight.png
│       └── chart_10_top_problem_combos.png
├── docs/
│   ├── phase-1-product-framing.md          <-- [PENDING: Phase 1]
│   ├── user_research.md                    <-- [PENDING: Phase 1]
│   ├── prd.md                              <-- [PENDING: Phase 1]
│   ├── metrics_framework.md                <-- [PENDING: Phase 1]
│   ├── ab_test_plan.md                     <-- [PENDING: Phase 1]
│   ├── data_dictionary.md                  <-- [PENDING: Phase 2]
│   ├── assumptions_and_limitations.md      <-- [PENDING: Phase 2]
│   └── interview_preparation.md            <-- [PENDING: Phase 5]
├── prototype/
│   ├── figma_wireframe_spec.md             <-- [PENDING: Phase 4]
│   ├── screen_1_product_page.md            <-- [PENDING: Phase 4]
│   ├── screen_2_size_recommendation.md      <-- [PENDING: Phase 4]
│   ├── screen_3_size_chart.md              <-- [PENDING: Phase 4]
│   └── prototype_preview.png               <-- [PENDING: Phase 4]
├── case-study/
│   └── final_case_study.md                 <-- [PENDING: Phase 5]
└── reports/
    ├── analysis_summary.md                 <-- [DONE: Initial markdown summary]
    ├── data_quality_report.md              <-- [PENDING: Phase 2]
    └── validation_report.md                <-- [PENDING: Phase 5]
```

---

## 3. VERIFIED DATA FACTS (GROUND TRUTH)

*All code, SQL queries, and written documentation must align with these verified metrics:*

| Metric / Parameter | Value | Reference / Derivation |
| :--- | :--- | :--- |
| **Total Processed Records** | **192,544** | `len(df)` |
| **Unique Users** | **105,571** | `df['user_id'].nunique()` |
| **Unique Catalog Items** | **5,850** | `df['item_id'].nunique()` |
| **Overall Fit Count / Pct** | **142,058 (73.78%)** | Feedback = 'fit' |
| **Reported "Small" Count / Pct** | **25,779 (13.39%)** | Feedback = 'small' |
| **Reported "Large" Count / Pct** | **24,707 (12.83%)** | Feedback = 'large' |
| **Non-Fit Count / Pct (Key KPI)**| **50,486 (26.22%)** | Feedback in ('small', 'large') |
| **Categories Count** | **68 unique** | Top: dress (92,884), gown (44,381), sheath (19,316) |
| **Body Types Count** | **7 unique** | Hourglass (55,349), athletic (43,667), pear (22,135), petite (22,131), full bust (15,006), straight & narrow (14,742), apple (4,877) |
| **Rating by Fit Satisfaction** | Fit: **9.25/10**, Small: **7.84/10**, Large: **7.92/10** | Shows distinct drop (~1.4 rating points) when fit fails |
| **Size Range** | **0 to 58** | Grouped into: XS, S, M, L, XL, XXL, XXXL+ |
| **Database Table & Rows** | `fit_feedback` in `fit_feedback.db` | **192,544 rows**, exactly matches CSV |

---

## 4. STEP-BY-STEP REMAINING WORK PLAN

To continue from any session, execute the remaining deliverables in five structured phases:

### Phase 1: Product Strategy, PRD & Experimentation (Folder: `docs/`)
1. **`phase-1-product-framing.md`**:
   - Problem framing: High return rate in Indian fashion e-commerce (30-40% of returns driven by size/fit mismatch).
   - Target personas: *Priya* (25, urban professional, buys from new D2C brands), *Meera* (35, buys for family, value-conscious), *Ananya* (22, first-time mobile apparel buyer).
   - Core Hypotheses: Proactive size guidance at point-of-decision reduces uncertainty without degrading conversion.
2. **`user_research.md`**:
   - Synthesis of quantitative findings from the dataset.
   - Qualitative insights from directional user interview protocols (common pain points: brand vanity sizing, lack of bust/waist measurement tape, return friction).
3. **`prd.md`**:
   - Comprehensive Product Requirements Document for **Myntra PDP Size Recommendation Experience**.
   - Functional specs (FR-001 to FR-012): Profile entry, smart size card, fit tendency indicator ("Runs slightly small"), confidence tag.
   - Non-functional specs (latency < 120ms, 99.9% uptime, responsive mobile UI).
   - Edge cases: Cold start items (< 30 reviews), users between two sizes, outliers.
4. **`metrics_framework.md`**:
   - Metric hierarchy using the Google HEART framework.
   - **North Star:** Fit-related return rate reduction.
   - **Leading Metrics:** Widget engagement rate, size recommendation adoption rate.
   - **Guardrails:** PDP-to-Add-to-Bag conversion rate, page load time (p95).
5. **`ab_test_plan.md`**:
   - Two-arm randomised controlled trial: Control (Standard PDP) vs Treatment (PDP + Size Recommendation).
   - Sample size calculation using Python `statsmodels` (assume baseline 20% size returns, target 18%, $\alpha=0.05$, $1-\beta=0.80 \rightarrow n \approx 4,374$ orders per arm).
   - Randomisation unit (user-level hash), duration (minimum 3-4 weeks to allow return-window clearance), guardrail breach tripwires.

### Phase 2: Data Quality & Governance (Folders: `data/`, `reports/`, `docs/`)
1. **`data/README.md`**: Dataset attribution (Misra et al., UCSD RecSys 2018), CC BY 4.0 license, storage structure, and reproducibility commands.
2. **`docs/data_dictionary.md`**: Tabular schema definitions covering all 15 raw columns and 20 engineered columns (types, descriptions, null handling, valid ranges).
3. **`docs/assumptions_and_limitations.md`**: Exhaustive documentation of rental proxy assumptions, self-reported measurement noise, lack of Indian ethnic wear in UCSD data, and cold-start boundaries.
4. **`reports/data_quality_report.md`**: Audit of missing values, duplicate checks (189 exact duplicates flagged), unit normalization log, and BMI sanity checks.

### Phase 3: Jupyter Notebook Suite (Folder: `notebooks/`)
Build clean, self-contained, reproducible `.ipynb` notebooks containing runnable Python code and markdown annotations:
1. **`01_data_understanding.ipynb`**: Data loading from `data/raw/`, schema validation, raw distributions, and nullity matrices.
2. **`02_data_cleaning.ipynb`**: Height string parsing (`5' 8"` $\rightarrow$ inches/cm), weight parsing (`137lbs` $\rightarrow$ numeric), body type standardization, and BMI computation.
3. **`03_exploratory_analysis.ipynb`**: Fit distribution, demographic breakdowns (age bands, body types), and rating correlation analysis.
4. **`04_fit_insights.ipynb`**: Category ranking by non-fit rate, category-size heatmap generation, and business recommendations.

### Phase 4: BI Dashboard & Prototype UI (Folders: `dashboard/`, `prototype/`)
1. **`dashboard/tableau_instructions.md`**:
   - Detailed guide to connect `dashboard_data.csv` in Tableau Public / Desktop.
   - Exact shelf configurations (Rows, Columns, Color marks, Filters) for 5 core sheets:
     - Sheet 1: Fit Breakdown Donut / Pie.
     - Sheet 2: Non-Fit Rate by Category (Bar Chart with 200+ N cutoff).
     - Sheet 3: Sizing Risk by Size Group (XS to XXXL+).
     - Sheet 4: Silhouette matrix (Body type vs Fit).
     - Sheet 5: Category × Size Non-Fit Heatmap.
2. **`dashboard/dashboard_metrics.md`**: Card-by-card KPI breakdown and filtering logic.
3. **`dashboard/dashboard_preview.png`**: Composite layout visual displaying the 5 core charts as a cohesive analytics dashboard.
4. **Mobile Prototype Specifications (`prototype/`)**:
   - `figma_wireframe_spec.md`: Color hex codes (#FF3F6C Myntra Rose, #282C3F Charcoal, #F5F5F6 Light Gray), typography scale, 8px layout grid, and Auto-Layout rules.
   - `screen_1_product_page.md`: Mobile PDP wireframe with size selector and inline recommendation prompt ("Not sure about your size? Get recommendation").
   - `screen_2_size_recommendation.md`: Modal bottom sheet asking for height/weight/body shape or displaying instant recommendation ("Recommended: Size M — 82% of customers with your profile felt comfortable").
   - `screen_3_size_chart.md`: Enhanced interactive size chart comparing garment measurements to customer body measurements.
   - `prototype_preview.png`: Visual multi-screen mockup showing the user flow.

### Phase 5: Final Case Study, Interview Prep & GitHub Repo (Folders: `case-study/`, `reports/`, Root)
1. **`case-study/final_case_study.md`**:
   - Executive portfolio piece: Title, Executive Summary, Problem Diagnosis, Data Findings, Product Solution, Experimentation Plan, and Key PM Takeaways.
2. **`docs/interview_preparation.md`**:
   - 60-second elevator pitch & 2-minute walkthrough.
   - Top 10 PM interview questions with model answers grounded in actual data numbers (e.g., "Why is conversion a guardrail?", "How do you handle cold-start products?", "How do you justify using rental data for Myntra?").
3. **`reports/validation_report.md`**:
   - Audit reconciling Python calculations against SQLite query results to prove mathematical consistency across tools.
4. **`requirements.txt`**:
   - Exact pinned versions (`pandas`, `numpy`, `matplotlib`, `statsmodels`, `seaborn`, `ipykernel`).
5. **`README.md`**:
   - Top-tier GitHub presentation with project badges, problem statement, key metrics callout cards, architecture diagram, file index, and replication instructions.

---

## 5. PROMPT INSTRUCTIONS FOR A NEW AGENT SESSION

If resuming this project in a fresh agent session, simply provide this prompt:

```text
I am continuing my portfolio project: "Myntra Size & Fit Analysis: PRD, Data Analysis, Dashboard & Prototype".
The project workspace is: c:\Users\champ\Desktop\Myntra-size and fit analysis\myntra-size-fit-analysis
Please inspect MASTER_PROJECT_PLAN.md in the project root.
The data acquisition, data cleaning (renttherunway_cleaned.csv), SQLite database (fit_feedback.db), charts (dashboard/charts/), and SQL scripts (sql/) are already completed and verified.
Please proceed autonomously with the next stages:
1. Author all strategy and product documents in docs/ (phase-1-product-framing.md, prd.md, ab_test_plan.md, metrics_framework.md, user_research.md, data_dictionary.md, assumptions_and_limitations.md, interview_preparation.md).
2. Generate the Jupyter notebooks in notebooks/ (01 to 04).
3. Complete dashboard documentation and preview in dashboard/.
4. Write prototype specifications and UI mockups in prototype/.
5. Produce the final case study in case-study/final_case_study.md, validation report in reports/, requirements.txt, and root README.md.
Execute all tasks directly using your tools.
```

---
*End of Master Execution & Handover Plan.*
