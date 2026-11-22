# Data Directory

## Source
**Rent the Runway Fit Feedback Dataset** — Misra et al., UCSD RecSys 2018.
- License: **CC-BY-4.0**
- Paper: *Decomposing Fit Semantics for Product Size Recommendation in Metric Spaces* (RecSys 2018)
- Download: https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit

## Structure
```
data/
├── raw/
│   ├── renttherunway_final_data.json   (192,544 records, ~117 MB)
│   └── modcloth_final_data.json        (downloaded with the dataset package)
└── processed/
    ├── renttherunway_cleaned.csv        (cleaned & feature-engineered, ~97 MB)
    ├── fit_feedback.db                  (SQLite database, ~117 MB)
    └── data_summary.json               (summary statistics)
```

## Reproducing from Scratch
```bash
python -m src.data_cleaning      # reads raw JSON → writes cleaned CSV + SQLite DB
python -m src.analysis           # reads DB → writes dashboard CSVs & charts
```

## Note on Large Files
The raw JSON, cleaned CSV, and SQLite DB exceed GitHub's 100 MB file-size limit and are listed in `.gitignore`. To obtain them:
1. Download the original dataset from the UCSD link above.
2. Place `renttherunway_final_data.json` in `data/raw/`.
3. Run the cleaning pipeline (`python -m src.data_cleaning`).
