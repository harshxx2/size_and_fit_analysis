# Analysis Summary Report

## Dataset Overview

| Metric | Value |
|--------|-------|
| Total Records | 192,544 |
| Unique Users | 105,571 |
| Unique Items | 5,850 |
| Categories | 68 |
| Body Types | 7 |
| Date Range | 2010 – 2018 |

## Overall Fit Distribution

| Fit Label | Count | Percentage |
|-----------|-------|------------|
| Fit | 142,058 | 73.8% |
| Small | 25,779 | 13.4% |
| Large | 24,707 | 12.8% |
| **Non-Fit (Small + Large)** | **50,486** | **26.2%** |

**Non-fit rate = (Small + Large) / Total valid fit records × 100 = 26.22%**

## Key Findings

### 1. Overall Non-Fit Rate
- **26.2%** of all fit feedback indicates a sizing problem.
- **13.4%** reported the item ran small; **12.8%** reported it ran large.
- The small and large rates are roughly balanced, suggesting sizing issues are bidirectional.

### 2. Category Insights
- Categories with highest non-fit rates represent the greatest opportunity for sizing guidance.
- Structured garments (e.g., jackets, blazers, coats) tend to have higher non-fit rates than flowing styles.
- Dresses and gowns (the largest categories) have moderate non-fit rates but drive the most absolute non-fit volume.

### 3. Size Insights
- Extreme sizes (XS, XXXL+) tend to have higher non-fit rates than mid-range sizes.
- This may indicate poorer standardisation at size extremes or greater uncertainty among shoppers in those ranges.

### 4. Body Type Insights
- Non-fit rates vary across body types, suggesting body shape affects fit experience.
- This supports the concept of body-type-aware size recommendations.

### 5. Rating Correlation
- Items that fit well receive substantially higher ratings (mean ~9.3) compared to non-fit items (small: ~8.4, large: ~8.6).
- This establishes a clear link between fit satisfaction and overall customer satisfaction.
- **Note**: This is a descriptive correlation, not a proven causal relationship.

### 6. Rental Occasion
- Different occasions show varying non-fit rates, possibly reflecting different garment types or sizing urgency.

## Data Limitations

1. **Dataset is from RentTheRunway**, a US-based rental platform — not Myntra transaction data.
2. **Non-fit rate is a proxy** for sizing problems, not an actual return rate.
3. **Self-reported body measurements** may contain inaccuracies.
4. **Rental context differs from purchase** — users may rent sizes they would not purchase.
5. **No Indian body-type data** — findings may not fully generalise to Indian consumers.
6. **Missing values** exist for body type (14,637), weight (29,982), bust size (18,411), and age (960).

## Methodology Notes

- **Minimum sample size**: n ≥ 50 required for subgroup analysis.
- **Non-fit rate**: (small + large) / total valid fit records × 100.
- **All findings are descriptive** — no causal claims are made.
- **Charts use actual dataset values** — no data has been fabricated.
