-- Schema for RentTheRunway Fit Feedback Database
-- Myntra Size & Fit Analysis Portfolio Project

CREATE TABLE IF NOT EXISTS fit_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fit TEXT NOT NULL,
    user_id INTEGER,
    bust_size TEXT,
    item_id INTEGER,
    weight TEXT,
    rating REAL,
    rented_for TEXT,
    review_text TEXT,
    body_type TEXT,
    review_summary TEXT,
    category TEXT,
    height TEXT,
    size INTEGER,
    age REAL,
    review_date TEXT,
    -- Engineered columns
    height_inches REAL,
    weight_lbs REAL,
    body_type_clean TEXT,
    category_clean TEXT,
    rented_for_clean TEXT,
    is_fit INTEGER,
    is_small INTEGER,
    is_large INTEGER,
    is_nonfit INTEGER,
    age_group TEXT,
    bmi REAL,
    size_category TEXT,
    bust_band REAL,
    bust_cup TEXT,
    review_year INTEGER,
    review_month INTEGER
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_fit ON fit_feedback(fit);
CREATE INDEX IF NOT EXISTS idx_category ON fit_feedback(category_clean);
CREATE INDEX IF NOT EXISTS idx_size ON fit_feedback(size);
CREATE INDEX IF NOT EXISTS idx_size_category ON fit_feedback(size_category);
CREATE INDEX IF NOT EXISTS idx_body_type ON fit_feedback(body_type_clean);
CREATE INDEX IF NOT EXISTS idx_rented_for ON fit_feedback(rented_for_clean);
CREATE INDEX IF NOT EXISTS idx_age_group ON fit_feedback(age_group);
CREATE INDEX IF NOT EXISTS idx_rating ON fit_feedback(rating);
