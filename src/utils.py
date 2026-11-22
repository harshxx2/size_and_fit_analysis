"""
Utility functions for the Myntra Size & Fit Analysis project.
"""

import pandas as pd
import numpy as np
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
CHARTS_DIR = os.path.join(BASE_DIR, 'dashboard', 'charts')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')

# Ensure dirs exist
for d in [CHARTS_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

# Minimum sample size for subgroup analysis
MIN_SAMPLE_SIZE = 50


def load_cleaned_data():
    """Load the cleaned dataset."""
    path = os.path.join(PROCESSED_DIR, 'renttherunway_cleaned.csv')
    df = pd.read_csv(path)
    return df


def non_fit_rate(group):
    """Calculate non-fit rate for a group."""
    total = len(group)
    if total < MIN_SAMPLE_SIZE:
        return pd.Series({
            'non_fit_rate': np.nan,
            'fit_rate': np.nan,
            'small_rate': np.nan,
            'large_rate': np.nan,
            'total_records': total,
            'sufficient_sample': False
        })
    non_fit = group['is_nonfit'].sum()
    fit = group['is_fit'].sum()
    small = group['is_small'].sum()
    large = group['is_large'].sum()
    return pd.Series({
        'non_fit_rate': round(non_fit / total * 100, 2),
        'fit_rate': round(fit / total * 100, 2),
        'small_rate': round(small / total * 100, 2),
        'large_rate': round(large / total * 100, 2),
        'total_records': total,
        'sufficient_sample': True
    })


def format_pct(value, decimals=1):
    """Format a percentage value."""
    if pd.isna(value):
        return 'N/A'
    return f'{value:.{decimals}f}%'


def category_order():
    """Return categories ordered by typical record count (for consistent charts)."""
    return [
        'dress', 'gown', 'sheath', 'shift', 'jumpsuit', 'top', 'maxi',
        'romper', 'jacket', 'mini', 'skirt', 'sweater', 'coat', 'blazer',
        'shirtdress', 'pants', 'shorts', 'blouse', 'cardigan', 'vest',
        'cape', 'kaftan', 'tunic', 'kimono'
    ]


def size_category_order():
    """Return size categories in order."""
    return ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL+']


def age_group_order():
    """Return age groups in order."""
    return ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']


def body_type_order():
    """Return body types in order."""
    return [
        'hourglass', 'athletic', 'pear', 'petite',
        'full bust', 'straight & narrow', 'apple'
    ]
