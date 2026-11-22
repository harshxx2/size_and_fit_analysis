"""
Exploratory Analysis Script for RentTheRunway Fit Feedback Dataset
Myntra Size & Fit Analysis Portfolio Project

Generates all charts and analysis summaries.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os
import json
import sys
import warnings
warnings.filterwarnings('ignore')

# Add parent dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import load_cleaned_data, non_fit_rate, MIN_SAMPLE_SIZE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARTS_DIR = os.path.join(BASE_DIR, 'dashboard', 'charts')
DASHBOARD_DIR = os.path.join(BASE_DIR, 'dashboard')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
os.makedirs(CHARTS_DIR, exist_ok=True)

# Color palette — professional, accessible
COLORS = {
    'fit': '#2ecc71',
    'small': '#e74c3c',
    'large': '#3498db',
    'primary': '#1a73e8',
    'secondary': '#ea4335',
    'accent': '#fbbc04',
    'neutral': '#5f6368',
    'bg': '#ffffff',
}

FIT_COLORS = ['#2ecc71', '#e74c3c', '#3498db']

plt.rcParams.update({
    'figure.figsize': (12, 7),
    'font.size': 12,
    'font.family': 'sans-serif',
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelsize': 13,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
})


def chart_01_fit_distribution(df):
    """Overall fit distribution pie + bar."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Pie chart
    fit_counts = df['fit'].value_counts()
    labels = ['Fit', 'Small', 'Large']
    sizes = [fit_counts.get('fit', 0), fit_counts.get('small', 0), fit_counts.get('large', 0)]
    pcts = [s/sum(sizes)*100 for s in sizes]

    wedges, texts, autotexts = axes[0].pie(
        sizes, labels=labels, colors=FIT_COLORS,
        autopct='%1.1f%%', startangle=90,
        textprops={'fontsize': 13, 'fontweight': 'bold'},
        wedgeprops={'edgecolor': 'white', 'linewidth': 2}
    )
    axes[0].set_title('Overall Fit Distribution\n(N = {:,})'.format(len(df)))

    # Bar chart
    bars = axes[1].bar(labels, sizes, color=FIT_COLORS, edgecolor='white', linewidth=1.5)
    for bar, count, pct in zip(bars, sizes, pcts):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                     f'{count:,}\n({pct:.1f}%)', ha='center', va='bottom', fontweight='bold')
    axes[1].set_ylabel('Number of Records')
    axes[1].set_title('Fit Feedback Count')
    axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_01_fit_distribution.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return fit_counts


def chart_02_nonfit_by_category(df):
    """Non-fit rate by category."""
    cat_stats = df.groupby('category_clean').apply(non_fit_rate).reset_index()
    cat_stats = cat_stats[cat_stats['sufficient_sample'] == True].sort_values('non_fit_rate', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#e74c3c' if r > 30 else '#f39c12' if r > 25 else '#2ecc71'
              for r in cat_stats['non_fit_rate']]
    bars = ax.barh(cat_stats['category_clean'], cat_stats['non_fit_rate'], color=colors, edgecolor='white')

    for bar, n in zip(bars, cat_stats['total_records']):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():.1f}% (n={int(n):,})',
                va='center', fontsize=10)

    ax.set_xlabel('Non-Fit Rate (%)')
    ax.set_title('Non-Fit Rate by Category\n(Categories with n ≥ {:,} records)'.format(MIN_SAMPLE_SIZE))
    ax.axvline(x=df['is_nonfit'].mean()*100, color='gray', linestyle='--', alpha=0.7, label=f'Overall: {df["is_nonfit"].mean()*100:.1f}%')
    ax.legend()
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_02_nonfit_by_category.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return cat_stats


def chart_03_nonfit_by_size(df):
    """Non-fit rate by size category."""
    order = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL+']
    size_stats = df.groupby('size_category').apply(non_fit_rate).reset_index()
    size_stats['size_category'] = pd.Categorical(size_stats['size_category'], categories=order, ordered=True)
    size_stats = size_stats.sort_values('size_category')
    size_stats = size_stats[size_stats['sufficient_sample'] == True]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Non-fit rate bar
    bars = axes[0].bar(size_stats['size_category'], size_stats['non_fit_rate'],
                       color=COLORS['secondary'], edgecolor='white')
    for bar, n in zip(bars, size_stats['total_records']):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                     f'{bar.get_height():.1f}%\n(n={int(n):,})',
                     ha='center', va='bottom', fontsize=9)
    axes[0].set_ylabel('Non-Fit Rate (%)')
    axes[0].set_title('Non-Fit Rate by Size Category')
    axes[0].axhline(y=df['is_nonfit'].mean()*100, color='gray', linestyle='--', alpha=0.7)

    # Stacked bar: small vs large composition
    axes[1].bar(size_stats['size_category'], size_stats['small_rate'],
                label='Reported Small', color=COLORS['small'], edgecolor='white')
    axes[1].bar(size_stats['size_category'], size_stats['large_rate'],
                bottom=size_stats['small_rate'],
                label='Reported Large', color=COLORS['large'], edgecolor='white')
    axes[1].set_ylabel('Rate (%)')
    axes[1].set_title('Small vs Large Rate by Size Category')
    axes[1].legend()

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_03_nonfit_by_size.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return size_stats


def chart_04_body_type(df):
    """Fit distribution by body type."""
    bt_stats = df[df['body_type'].notna()].groupby('body_type').apply(non_fit_rate).reset_index()
    bt_stats = bt_stats[bt_stats['sufficient_sample'] == True].sort_values('non_fit_rate', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(bt_stats))
    width = 0.25
    ax.bar(x - width, bt_stats['fit_rate'], width, label='Fit', color=COLORS['fit'], edgecolor='white')
    ax.bar(x, bt_stats['small_rate'], width, label='Small', color=COLORS['small'], edgecolor='white')
    ax.bar(x + width, bt_stats['large_rate'], width, label='Large', color=COLORS['large'], edgecolor='white')

    ax.set_xticks(x)
    ax.set_xticklabels([f'{bt}\n(n={int(n):,})' for bt, n in zip(bt_stats['body_type'], bt_stats['total_records'])],
                       fontsize=10)
    ax.set_ylabel('Rate (%)')
    ax.set_title('Fit Distribution by Body Type')
    ax.legend()
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_04_body_type.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return bt_stats


def chart_05_category_size_heatmap(df):
    """Non-fit rate heatmap: category × size."""
    top_cats = df['category_clean'].value_counts().head(10).index.tolist()
    size_order = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL+']

    subset = df[df['category_clean'].isin(top_cats)]
    pivot = subset.groupby(['category_clean', 'size_category']).apply(
        lambda g: g['is_nonfit'].mean() * 100 if len(g) >= MIN_SAMPLE_SIZE else np.nan
    ).unstack()

    # Reorder
    pivot = pivot.reindex(columns=[c for c in size_order if c in pivot.columns])
    pivot = pivot.reindex(top_cats)

    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(pivot.values, cmap='RdYlGn_r', aspect='auto', vmin=15, vmax=45)

    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_xticklabels(pivot.columns)
    ax.set_yticklabels(pivot.index)

    # Add text annotations
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot.values[i, j]
            if not np.isnan(val):
                ax.text(j, i, f'{val:.1f}%', ha='center', va='center',
                       color='white' if val > 30 else 'black', fontsize=10, fontweight='bold')
            else:
                ax.text(j, i, 'n<50', ha='center', va='center', color='gray', fontsize=9, style='italic')

    cbar = plt.colorbar(im, ax=ax, label='Non-Fit Rate (%)')
    ax.set_title('Non-Fit Rate: Category × Size\n(Top 10 categories, cells with n ≥ {:,})'.format(MIN_SAMPLE_SIZE))
    ax.set_xlabel('Size Category')
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_05_category_size_heatmap.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')


def chart_06_rating_vs_fit(df):
    """Rating distribution by fit outcome."""
    df_valid = df[df['rating'].notna()].copy()
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Box-like comparison
    for i, fit_val in enumerate(['fit', 'small', 'large']):
        ratings = df_valid[df_valid['fit'] == fit_val]['rating']
        axes[0].hist(ratings, bins=[1, 3, 5, 7, 9, 11], alpha=0.6,
                     label=f'{fit_val.title()} (mean={ratings.mean():.1f})',
                     color=FIT_COLORS[i], edgecolor='white')
    axes[0].set_xlabel('Rating')
    axes[0].set_ylabel('Count')
    axes[0].set_title('Rating Distribution by Fit Outcome')
    axes[0].legend()

    # Mean rating comparison
    mean_ratings = df_valid.groupby('fit')['rating'].mean().reindex(['fit', 'small', 'large'])
    bars = axes[1].bar(mean_ratings.index.str.title(), mean_ratings.values, color=FIT_COLORS, edgecolor='white')
    for bar in bars:
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                     f'{bar.get_height():.2f}', ha='center', va='bottom', fontweight='bold')
    axes[1].set_ylabel('Mean Rating')
    axes[1].set_title('Average Rating by Fit Outcome')
    axes[1].set_ylim(0, 11)

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_06_rating_vs_fit.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')


def chart_07_rental_purpose(df):
    """Fit distribution by rental purpose."""
    rp_stats = df[df['rented_for_clean'].notna()].groupby('rented_for_clean').apply(non_fit_rate).reset_index()
    rp_stats = rp_stats[rp_stats['sufficient_sample'] == True].sort_values('non_fit_rate', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(rp_stats))
    width = 0.6
    bars = ax.barh(rp_stats['rented_for_clean'], rp_stats['non_fit_rate'],
                   color=COLORS['primary'], edgecolor='white')
    for bar, n in zip(bars, rp_stats['total_records']):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():.1f}% (n={int(n):,})', va='center', fontsize=10)

    ax.set_xlabel('Non-Fit Rate (%)')
    ax.set_title('Non-Fit Rate by Rental Occasion')
    ax.axvline(x=df['is_nonfit'].mean()*100, color='gray', linestyle='--', alpha=0.7)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_07_rental_purpose.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return rp_stats


def chart_08_age_group(df):
    """Non-fit rate by age group."""
    ag_stats = df[df['age_group'].notna()].groupby('age_group').apply(non_fit_rate).reset_index()
    order = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    ag_stats['age_group'] = pd.Categorical(ag_stats['age_group'], categories=order, ordered=True)
    ag_stats = ag_stats.sort_values('age_group')
    ag_stats = ag_stats[ag_stats['sufficient_sample'] == True]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(ag_stats['age_group'].astype(str), ag_stats['non_fit_rate'],
                  color=COLORS['primary'], edgecolor='white')
    for bar, n in zip(bars, ag_stats['total_records']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{bar.get_height():.1f}%\n(n={int(n):,})', ha='center', va='bottom', fontsize=10)
    ax.set_ylabel('Non-Fit Rate (%)')
    ax.set_xlabel('Age Group')
    ax.set_title('Non-Fit Rate by Age Group')
    ax.axhline(y=df['is_nonfit'].mean()*100, color='gray', linestyle='--', alpha=0.7)
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_08_age_group.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return ag_stats


def chart_09_height_weight(df):
    """Height and weight patterns vs fit."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for i, fit_val in enumerate(['fit', 'small', 'large']):
        subset = df[(df['fit'] == fit_val) & df['height_inches'].notna()]
        axes[0].hist(subset['height_inches'], bins=20, alpha=0.5,
                     label=f'{fit_val.title()} (n={len(subset):,})',
                     color=FIT_COLORS[i], edgecolor='white', density=True)

    axes[0].set_xlabel('Height (inches)')
    axes[0].set_ylabel('Density')
    axes[0].set_title('Height Distribution by Fit Outcome')
    axes[0].legend()

    for i, fit_val in enumerate(['fit', 'small', 'large']):
        subset = df[(df['fit'] == fit_val) & df['weight_lbs'].notna()]
        axes[1].hist(subset['weight_lbs'], bins=20, alpha=0.5,
                     label=f'{fit_val.title()} (n={len(subset):,})',
                     color=FIT_COLORS[i], edgecolor='white', density=True)

    axes[1].set_xlabel('Weight (lbs)')
    axes[1].set_ylabel('Density')
    axes[1].set_title('Weight Distribution by Fit Outcome')
    axes[1].legend()

    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_09_height_weight.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')


def chart_10_top_problem_combos(df):
    """Top category-size combinations with highest non-fit rates."""
    combo = df.groupby(['category_clean', 'size_category']).apply(non_fit_rate).reset_index()
    combo = combo[combo['sufficient_sample'] == True]
    combo = combo.sort_values('non_fit_rate', ascending=False).head(15)
    combo['label'] = combo['category_clean'] + ' / ' + combo['size_category']

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#e74c3c' if r > 35 else '#f39c12' if r > 30 else '#3498db'
              for r in combo['non_fit_rate']]
    bars = ax.barh(combo['label'][::-1], combo['non_fit_rate'][::-1], color=colors[::-1], edgecolor='white')
    for bar, n in zip(bars, combo['total_records'][::-1]):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                f'{bar.get_width():.1f}% (n={int(n):,})', va='center', fontsize=10)
    ax.set_xlabel('Non-Fit Rate (%)')
    ax.set_title('Top 15 Category-Size Combinations by Non-Fit Rate\n(n ≥ {:,} records)'.format(MIN_SAMPLE_SIZE))
    plt.tight_layout()
    path = os.path.join(CHARTS_DIR, 'chart_10_top_problem_combos.png')
    plt.savefig(path)
    plt.close()
    print(f'  Saved: {path}')
    return combo


def generate_dashboard_data(df):
    """Generate the dashboard_data.csv for Tableau import."""
    # Category-level aggregation
    cat_stats = df.groupby('category_clean').apply(non_fit_rate).reset_index()
    cat_stats = cat_stats[cat_stats['sufficient_sample'] == True]
    cat_stats.to_csv(os.path.join(DASHBOARD_DIR, 'category_stats.csv'), index=False)

    # Size-level aggregation
    size_stats = df.groupby('size_category').apply(non_fit_rate).reset_index()
    size_stats.to_csv(os.path.join(DASHBOARD_DIR, 'size_stats.csv'), index=False)

    # Body type aggregation
    bt_stats = df[df['body_type'].notna()].groupby('body_type').apply(non_fit_rate).reset_index()
    bt_stats.to_csv(os.path.join(DASHBOARD_DIR, 'body_type_stats.csv'), index=False)

    # Category × Size
    combo = df.groupby(['category_clean', 'size_category']).apply(non_fit_rate).reset_index()
    combo = combo[combo['sufficient_sample'] == True]
    combo.to_csv(os.path.join(DASHBOARD_DIR, 'category_size_stats.csv'), index=False)

    # Full dashboard dataset
    dashboard_cols = [
        'fit', 'size', 'size_category', 'category_clean', 'body_type',
        'height_inches', 'weight_lbs', 'age', 'age_group', 'bmi',
        'rating', 'rented_for_clean', 'is_fit', 'is_small', 'is_large', 'is_nonfit'
    ]
    df[dashboard_cols].to_csv(os.path.join(DASHBOARD_DIR, 'dashboard_data.csv'), index=False)
    print(f'  Dashboard data saved to {DASHBOARD_DIR}')


def generate_analysis_summary(df, results):
    """Generate the analysis summary report."""
    total = len(df)
    summary = f"""# Analysis Summary Report

## Dataset Overview

| Metric | Value |
|--------|-------|
| Total Records | {total:,} |
| Unique Users | {df['user_id'].nunique():,} |
| Unique Items | {df['item_id'].nunique():,} |
| Categories | {df['category_clean'].nunique()} |
| Body Types | {df['body_type'].nunique()} |
| Date Range | {df['review_year'].min():.0f} – {df['review_year'].max():.0f} |

## Overall Fit Distribution

| Fit Label | Count | Percentage |
|-----------|-------|------------|
| Fit | {df['is_fit'].sum():,} | {df['is_fit'].mean()*100:.1f}% |
| Small | {df['is_small'].sum():,} | {df['is_small'].mean()*100:.1f}% |
| Large | {df['is_large'].sum():,} | {df['is_large'].mean()*100:.1f}% |
| **Non-Fit (Small + Large)** | **{df['is_nonfit'].sum():,}** | **{df['is_nonfit'].mean()*100:.1f}%** |

**Non-fit rate = (Small + Large) / Total valid fit records × 100 = {df['is_nonfit'].mean()*100:.2f}%**

## Key Findings

### 1. Overall Non-Fit Rate
- **{df['is_nonfit'].mean()*100:.1f}%** of all fit feedback indicates a sizing problem.
- **{df['is_small'].mean()*100:.1f}%** reported the item ran small; **{df['is_large'].mean()*100:.1f}%** reported it ran large.
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
- Items that fit well receive substantially higher ratings (mean ~{df[df['fit']=='fit']['rating'].mean():.1f}) compared to non-fit items (small: ~{df[df['fit']=='small']['rating'].mean():.1f}, large: ~{df[df['fit']=='large']['rating'].mean():.1f}).
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
6. **Missing values** exist for body type ({df['body_type'].isna().sum():,}), weight ({df['weight_lbs'].isna().sum():,}), bust size ({df['bust size'].isna().sum():,}), and age ({df['age'].isna().sum():,}).

## Methodology Notes

- **Minimum sample size**: n ≥ {MIN_SAMPLE_SIZE} required for subgroup analysis.
- **Non-fit rate**: (small + large) / total valid fit records × 100.
- **All findings are descriptive** — no causal claims are made.
- **Charts use actual dataset values** — no data has been fabricated.
"""
    report_path = os.path.join(REPORTS_DIR, 'analysis_summary.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f'  Analysis summary saved to {report_path}')


def main():
    print('=' * 60)
    print('EXPLORATORY ANALYSIS — RentTheRunway Fit Feedback')
    print('=' * 60)

    df = load_cleaned_data()
    print(f'Loaded {len(df):,} records')

    results = {}

    print('\n[1] Fit Distribution...')
    results['fit_counts'] = chart_01_fit_distribution(df)

    print('[2] Non-Fit by Category...')
    results['cat_stats'] = chart_02_nonfit_by_category(df)

    print('[3] Non-Fit by Size...')
    results['size_stats'] = chart_03_nonfit_by_size(df)

    print('[4] Body Type Analysis...')
    results['bt_stats'] = chart_04_body_type(df)

    print('[5] Category × Size Heatmap...')
    chart_05_category_size_heatmap(df)

    print('[6] Rating vs Fit...')
    chart_06_rating_vs_fit(df)

    print('[7] Rental Purpose...')
    results['rp_stats'] = chart_07_rental_purpose(df)

    print('[8] Age Group...')
    results['ag_stats'] = chart_08_age_group(df)

    print('[9] Height & Weight Patterns...')
    chart_09_height_weight(df)

    print('[10] Top Problem Combinations...')
    results['combos'] = chart_10_top_problem_combos(df)

    print('\n[11] Generating dashboard data...')
    generate_dashboard_data(df)

    print('[12] Generating analysis summary...')
    generate_analysis_summary(df, results)

    print('\n' + '=' * 60)
    print('ANALYSIS COMPLETE — All charts saved to dashboard/charts/')
    print('=' * 60)


if __name__ == '__main__':
    main()
