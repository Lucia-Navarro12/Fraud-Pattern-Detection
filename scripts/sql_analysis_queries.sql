
-- Query 1: Basic Statistics by Fraud Type

SELECT 
    Class,
    COUNT(*) as transaction_count,
    AVG(Amount) as avg_amount,
    MIN(Amount) as min_amount,
    MAX(Amount) as max_amount,
    STDDEV(Amount) as std_amount
FROM transactions
GROUP BY Class;

-- Query 2: Fraud Rate by Amount Ranges

SELECT 
    CASE 
        WHEN Amount < 50 THEN '0-50'
        WHEN Amount BETWEEN 50 AND 200 THEN '50-200'
        WHEN Amount BETWEEN 200 AND 500 THEN '200-500'
        ELSE '500+'
    END as amount_range,
    COUNT(*) as total_transactions,
    SUM(Class) as fraudulent_transactions,
    ROUND(SUM(Class) * 100.0 / COUNT(*), 4) as fraud_rate
FROM transactions
GROUP BY amount_range
ORDER BY amount_range;

-- Query 3: Time-Based Analysis

SELECT 
    FLOOR(Time / 3600) % 24 as hour_of_day,
    COUNT(*) as total_transactions,
    SUM(Class) as fraudulent_transactions,
    ROUND(SUM(Class) * 100.0 / COUNT(*), 4) as fraud_rate
FROM transactions
GROUP BY hour_of_day
ORDER BY hour_of_day;

-- Query 4: Top Fraud Hours

SELECT 
    FLOOR(Time / 3600) % 24 as hour_of_day,
    COUNT(*) as total_transactions,
    SUM(Class) as fraudulent_count,
    ROUND(SUM(Class) * 100.0 / COUNT(*), 4) as fraud_rate
FROM transactions
GROUP BY hour_of_day
HAVING COUNT(*) > 1000
ORDER BY fraud_rate DESC
LIMIT 10;