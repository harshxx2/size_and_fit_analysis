-- Size Analysis
-- Non-fit rate by size and size category

-- Non-fit rate by size category
SELECT
    size_category,
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
GROUP BY size_category
HAVING COUNT(*) >= 50
ORDER BY
    CASE size_category
        WHEN 'XS' THEN 1
        WHEN 'S' THEN 2
        WHEN 'M' THEN 3
        WHEN 'L' THEN 4
        WHEN 'XL' THEN 5
        WHEN 'XXL' THEN 6
        WHEN 'XXXL+' THEN 7
    END;

-- Non-fit rate by raw size (top 15 by volume)
SELECT
    size,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate
FROM fit_feedback
GROUP BY size
HAVING COUNT(*) >= 50
ORDER BY total_records DESC
LIMIT 15;

-- Category-Size combination analysis (top problem areas)
SELECT
    category_clean AS category,
    size_category,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate
FROM fit_feedback
GROUP BY category_clean, size_category
HAVING COUNT(*) >= 50
ORDER BY nonfit_rate DESC
LIMIT 20;
