-- Category Analysis
-- Non-fit rate by garment category

-- Overall fit summary by category
SELECT
    category_clean AS category,
    COUNT(*) AS total_records,
    SUM(is_fit) AS fit_count,
    SUM(is_small) AS small_count,
    SUM(is_large) AS large_count,
    SUM(is_nonfit) AS nonfit_count,
    ROUND(SUM(is_fit) * 100.0 / COUNT(*), 2) AS fit_rate,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate,
    ROUND(AVG(rating), 2) AS avg_rating
FROM fit_feedback
GROUP BY category_clean
HAVING COUNT(*) >= 50
ORDER BY nonfit_rate DESC;

-- Top 10 categories by volume
SELECT
    category_clean AS category,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate
FROM fit_feedback
GROUP BY category_clean
ORDER BY total_records DESC
LIMIT 10;

-- Categories where non-fit rate exceeds overall average
SELECT
    category_clean AS category,
    COUNT(*) AS total_records,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate
FROM fit_feedback
GROUP BY category_clean
HAVING COUNT(*) >= 50
   AND SUM(is_nonfit) * 100.0 / COUNT(*) > (
       SELECT SUM(is_nonfit) * 100.0 / COUNT(*) FROM fit_feedback
   )
ORDER BY nonfit_rate DESC;
