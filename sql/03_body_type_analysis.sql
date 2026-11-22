-- Body Type Analysis
-- Fit patterns across different body types

-- Non-fit rate by body type
SELECT
    body_type_clean AS body_type,
    COUNT(*) AS total_records,
    SUM(is_fit) AS fit_count,
    SUM(is_small) AS small_count,
    SUM(is_large) AS large_count,
    SUM(is_nonfit) AS nonfit_count,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate,
    ROUND(AVG(rating), 2) AS avg_rating
FROM fit_feedback
WHERE body_type_clean IS NOT NULL
GROUP BY body_type_clean
HAVING COUNT(*) >= 50
ORDER BY nonfit_rate DESC;

-- Body type × Category analysis
SELECT
    body_type_clean AS body_type,
    category_clean AS category,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate
FROM fit_feedback
WHERE body_type_clean IS NOT NULL
GROUP BY body_type_clean, category_clean
HAVING COUNT(*) >= 50
ORDER BY body_type_clean, nonfit_rate DESC;

-- Body type × Size category analysis
SELECT
    body_type_clean AS body_type,
    size_category,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate
FROM fit_feedback
WHERE body_type_clean IS NOT NULL
GROUP BY body_type_clean, size_category
HAVING COUNT(*) >= 50
ORDER BY body_type_clean, nonfit_rate DESC;

-- Height and weight summary by body type
SELECT
    body_type_clean AS body_type,
    COUNT(*) AS total_records,
    ROUND(AVG(height_inches), 1) AS avg_height_inches,
    ROUND(AVG(weight_lbs), 1) AS avg_weight_lbs,
    ROUND(AVG(bmi), 1) AS avg_bmi
FROM fit_feedback
WHERE body_type_clean IS NOT NULL
  AND height_inches IS NOT NULL
  AND weight_lbs IS NOT NULL
GROUP BY body_type_clean
ORDER BY avg_bmi;
