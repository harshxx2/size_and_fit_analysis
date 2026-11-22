"""
Data Cleaning Script for RentTheRunway Fit Feedback Dataset
Myntra Size & Fit Analysis Portfolio Project

This script loads the raw RentTheRunway dataset, performs cleaning and
feature engineering, and outputs a processed CSV for analysis.

Dataset: RentTheRunway Fit Feedback Dataset (Misra et al., UCSD)
License: CC BY 4.0
Source: https://www.kaggle.com/datasets/rmisra/clothing-fit-dataset-for-size-recommendation
"""

import pandas as pd
import numpy as np
import json
import os
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA = os.path.join(BASE_DIR, 'data', 'raw', 'renttherunway_final_data.json')
PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
OUTPUT_CSV = os.path.join(PROCESSED_DIR, 'renttherunway_cleaned.csv')
SUMMARY_JSON = os.path.join(PROCESSED_DIR, 'data_summary.json')

os.makedirs(PROCESSED_DIR, exist_ok=True)


def parse_height(h):
    """Parse height string like '5\' 8\"' to total inches."""
    if pd.isna(h):
        return np.nan
    h = str(h).strip()
    # Remove special quote characters
    h = h.replace('\u2033', '"').replace('\u2032', "'").replace('\u201d', '"').replace('\u2019', "'")
    if "'" in h:
        parts = h.replace('"', '').split("'")
        try:
            feet = int(parts[0].strip())
            inches = int(parts[1].strip()) if len(parts) > 1 and parts[1].strip() else 0
            return feet * 12 + inches
        except (ValueError, IndexError):
            return np.nan
    return np.nan


def parse_weight(w):
    """Parse weight string like '137lbs' to numeric pounds."""
    if pd.isna(w):
        return np.nan
    w = str(w).strip().lower().replace('lbs', '').replace('lb', '').strip()
    try:
        return float(w)
    except ValueError:
        return np.nan


def parse_bust(b):
    """Parse bust size like '34d' into band (int) and cup (str)."""
    if pd.isna(b):
        return np.nan, np.nan
    b = str(b).strip().lower()
    band = ''
    cup = ''
    for c in b:
        if c.isdigit():
            band += c
        elif c.isalpha():
            cup += c
    try:
        return int(band), cup
    except ValueError:
        return np.nan, np.nan


def age_group(a):
    """Categorize age into groups."""
    if pd.isna(a) or a < 10 or a > 100:
        return np.nan
    if a < 25:
        return '18-24'
    if a < 35:
        return '25-34'
    if a < 45:
        return '35-44'
    if a < 55:
        return '45-54'
    if a < 65:
        return '55-64'
    return '65+'


def size_category(s):
    """Map numeric size to standard size categories."""
    if s <= 4:
        return 'XS'
    if s <= 8:
        return 'S'
    if s <= 12:
        return 'M'
    if s <= 16:
        return 'L'
    if s <= 20:
        return 'XL'
    if s <= 24:
        return 'XXL'
    return 'XXXL+'


def main():
    print('=' * 60)
    print('DATA CLEANING — RentTheRunway Fit Feedback Dataset')
    print('=' * 60)

    # Load raw data
    print('\n[1] Loading raw data...')
    df = pd.read_json(RAW_DATA, lines=True)
    print(f'    Loaded {df.shape[0]:,} records with {df.shape[1]} columns')
    print(f'    Columns: {list(df.columns)}')

    # --- Missing Value Analysis ---
    print('\n[2] Missing value analysis:')
    missing = df.isnull().sum()
    for col in df.columns:
        pct = missing[col] / len(df) * 100
        print(f'    {col:20s}: {missing[col]:6,} ({pct:.1f}%)')

    # --- Parse Height ---
    print('\n[3] Parsing height...')
    df['height_inches'] = df['height'].apply(parse_height)
    valid_h = df['height_inches'].notna().sum()
    print(f'    Valid heights: {valid_h:,} ({valid_h/len(df)*100:.1f}%)')
    print(f'    Height range: {df["height_inches"].min():.0f}" - {df["height_inches"].max():.0f}"')

    # --- Parse Weight ---
    print('\n[4] Parsing weight...')
    df['weight_lbs'] = df['weight'].apply(parse_weight)
    valid_w = df['weight_lbs'].notna().sum()
    print(f'    Valid weights: {valid_w:,} ({valid_w/len(df)*100:.1f}%)')
    print(f'    Weight range: {df["weight_lbs"].min():.0f} - {df["weight_lbs"].max():.0f} lbs')

    # --- Clean Body Type ---
    print('\n[5] Cleaning body type...')
    df['body_type'] = df['body type'].str.strip().str.lower()
    print(f'    Body types: {df["body_type"].nunique()} unique')
    print(f'    Distribution:\n{df["body_type"].value_counts().to_string()}')

    # --- Clean Category ---
    print('\n[6] Cleaning category...')
    df['category_clean'] = df['category'].str.strip().str.lower()
    print(f'    Categories: {df["category_clean"].nunique()} unique')

    # --- Clean Rented For ---
    print('\n[7] Cleaning rented_for...')
    df['rented_for_clean'] = df['rented for'].str.strip().str.lower()
    df['rented_for_clean'] = df['rented_for_clean'].replace('party: cocktail', 'party')
    print(f'    Occasions: {df["rented_for_clean"].nunique()} unique')

    # --- Create Fit Indicators ---
    print('\n[8] Creating fit indicator columns...')
    df['is_fit'] = (df['fit'] == 'fit').astype(int)
    df['is_small'] = (df['fit'] == 'small').astype(int)
    df['is_large'] = (df['fit'] == 'large').astype(int)
    df['is_nonfit'] = (df['fit'] != 'fit').astype(int)

    total = len(df)
    fit_count = df['is_fit'].sum()
    small_count = df['is_small'].sum()
    large_count = df['is_large'].sum()
    nonfit_count = df['is_nonfit'].sum()
    print(f'    Fit:     {fit_count:,} ({fit_count/total*100:.1f}%)')
    print(f'    Small:   {small_count:,} ({small_count/total*100:.1f}%)')
    print(f'    Large:   {large_count:,} ({large_count/total*100:.1f}%)')
    print(f'    Non-fit: {nonfit_count:,} ({nonfit_count/total*100:.2f}%)')

    # --- Age Groups ---
    print('\n[9] Creating age groups...')
    df['age_group'] = df['age'].apply(age_group)
    print(f'    Age group distribution:\n{df["age_group"].value_counts().sort_index().to_string()}')

    # --- BMI Calculation ---
    print('\n[10] Calculating BMI...')
    df['bmi'] = (df['weight_lbs'] * 703) / (df['height_inches'] ** 2)
    # Cap unreasonable BMI
    unreasonable = ((df['bmi'] < 10) | (df['bmi'] > 70)).sum()
    df.loc[(df['bmi'] < 10) | (df['bmi'] > 70), 'bmi'] = np.nan
    print(f'    Valid BMI values: {df["bmi"].notna().sum():,}')
    print(f'    BMI range: {df["bmi"].min():.1f} - {df["bmi"].max():.1f}')
    print(f'    Unreasonable BMI removed: {unreasonable}')

    # --- Size Categories ---
    print('\n[11] Creating size categories...')
    df['size_category'] = df['size'].apply(size_category)
    print(f'    Size category distribution:\n{df["size_category"].value_counts().to_string()}')

    # --- Parse Bust Size ---
    print('\n[12] Parsing bust size...')
    bust_parsed = df['bust size'].apply(parse_bust)
    df['bust_band'] = bust_parsed.apply(lambda x: x[0])
    df['bust_cup'] = bust_parsed.apply(lambda x: x[1])
    print(f'    Valid bust sizes: {df["bust_band"].notna().sum():,}')

    # --- Parse Review Date ---
    print('\n[13] Parsing review dates...')
    df['review_date_parsed'] = pd.to_datetime(df['review_date'], format='mixed', errors='coerce')
    df['review_year'] = df['review_date_parsed'].dt.year
    df['review_month'] = df['review_date_parsed'].dt.month
    print(f'    Valid dates: {df["review_date_parsed"].notna().sum():,}')
    print(f'    Date range: {df["review_date_parsed"].min()} to {df["review_date_parsed"].max()}')

    # --- Duplicate Check ---
    print('\n[14] Checking duplicates...')
    full_dupes = df.duplicated().sum()
    subset_dupes = df.duplicated(subset=['user_id', 'item_id', 'fit', 'rating']).sum()
    print(f'    Full duplicates: {full_dupes}')
    print(f'    User-item-fit-rating duplicates: {subset_dupes}')

    # --- Outlier Flagging ---
    print('\n[15] Flagging outliers...')
    df['valid_age'] = ((df['age'] >= 10) & (df['age'] <= 100)) | df['age'].isna()
    invalid_age_count = (~df['valid_age']).sum()
    print(f'    Invalid age records: {invalid_age_count}')

    df['valid_height'] = ((df['height_inches'] >= 48) & (df['height_inches'] <= 84)) | df['height_inches'].isna()
    invalid_height = (~df['valid_height']).sum()
    print(f'    Invalid height records: {invalid_height}')

    df['valid_weight'] = ((df['weight_lbs'] >= 70) & (df['weight_lbs'] <= 400)) | df['weight_lbs'].isna()
    invalid_weight = (~df['valid_weight']).sum()
    print(f'    Invalid weight records: {invalid_weight}')

    # --- Save Cleaned Data ---
    print('\n[16] Saving cleaned data...')
    # Drop the parsed date column (not CSV-friendly timezone)
    save_cols = [c for c in df.columns if c != 'review_date_parsed']
    df[save_cols].to_csv(OUTPUT_CSV, index=False)
    file_size = os.path.getsize(OUTPUT_CSV)
    print(f'    Saved to: {OUTPUT_CSV}')
    print(f'    File size: {file_size/1024/1024:.1f} MB')
    print(f'    Final shape: {df.shape}')

    # --- Save Summary ---
    summary = {
        'total_records': int(df.shape[0]),
        'total_columns': int(df.shape[1]),
        'fit_distribution': {
            'fit': int(fit_count),
            'small': int(small_count),
            'large': int(large_count)
        },
        'non_fit_rate_pct': round(float(nonfit_count / total * 100), 2),
        'fit_rate_pct': round(float(fit_count / total * 100), 2),
        'missing_values': {
            'fit': 0,
            'rating': int(df['rating'].isna().sum()),
            'body_type': int(df['body_type'].isna().sum()),
            'height_inches': int(df['height_inches'].isna().sum()),
            'weight_lbs': int(df['weight_lbs'].isna().sum()),
            'age': int(df['age'].isna().sum()),
            'category': 0,
            'rented_for': int(df['rented_for_clean'].isna().sum()),
        },
        'categories_count': int(df['category_clean'].nunique()),
        'body_types_count': int(df['body_type'].nunique()),
        'size_range': [int(df['size'].min()), int(df['size'].max())],
        'age_range': [float(df['age'].dropna().min()), float(df['age'].dropna().max())],
        'height_range_inches': [float(df['height_inches'].dropna().min()), float(df['height_inches'].dropna().max())],
        'weight_range_lbs': [float(df['weight_lbs'].dropna().min()), float(df['weight_lbs'].dropna().max())],
        'unique_users': int(df['user_id'].nunique()),
        'unique_items': int(df['item_id'].nunique()),
        'date_range': [str(df['review_date_parsed'].min().date()), str(df['review_date_parsed'].max().date())],
        'full_duplicates': int(full_dupes),
    }
    with open(SUMMARY_JSON, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f'\n    Summary saved to: {SUMMARY_JSON}')

    # Print final summary
    print('\n' + '=' * 60)
    print('CLEANING COMPLETE')
    print('=' * 60)
    for k, v in summary.items():
        print(f'  {k}: {v}')

    return df, summary


if __name__ == '__main__':
    main()
