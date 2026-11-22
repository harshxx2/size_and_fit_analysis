-- 04_fit_summary.sql
-- Overall fit summary, ranking, and validation queries

-- 1. Overall Fit Feedback Metrics
SELECT 
    COUNT(*) AS total_records,
    SUM(is_fit) AS fit_count,
    SUM(is_small) AS small_count,
    SUM(is_large) AS large_count,
    SUM(is_nonfit) AS nonfit_count,
    ROUND(SUM(is_fit) * 100.0 / COUNT(*), 2) AS fit_rate_pct,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS nonfit_rate_pct,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_rate_pct,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_rate_pct,
    ROUND(AVG(rating), 2) AS avg_rating
FROM fit_feedback;

-- 2. Rating vs Fit Satisfaction
SELECT 
    fit,
    COUNT(*) AS review_count,
    ROUND(AVG(rating), 2) AS mean_rating,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM fit_feedback WHERE rating IS NOT NULL), 2) AS pct_of_rated_reviews
FROM fit_feedback
WHERE rating IS NOT NULL
GROUP BY fit
ORDER BY mean_rating DESC;

-- 3. Top Problem Categories Ranked by Non-Fit Rate (Minimum 200 records)
SELECT 
    category_clean AS category,
    COUNT(*) AS sample_size,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS non_fit_pct,
    ROUND(SUM(is_small) * 100.0 / COUNT(*), 2) AS small_pct,
    ROUND(SUM(is_large) * 100.0 / COUNT(*), 2) AS large_pct,
    DENSE_RANK() OVER (ORDER BY ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) DESC) AS problem_rank
FROM fit_feedback
GROUP BY category_clean
HAVING COUNT(*) >= 200
ORDER BY non_fit_pct DESC;

-- 4. Fit Breakdown by Rented Occasion
SELECT 
    COALESCE(rented_for_clean, 'unknown') AS occasion,
    COUNT(*) AS sample_size,
    ROUND(SUM(is_nonfit) * 100.0 / COUNT(*), 2) AS non_fit_pct,
    ROUND(SUM(is_fit) * 100.0 / COUNT(*), 2) AS fit_pct,
    ROUND(AVG(rating), 2) AS avg_rating
FROM fit_feedback
GROUP BY rented_for_clean
HAVING COUNT(*) >= 100
ORDER BY non_fit_pct DESC;
