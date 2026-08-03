SELECT
    market_segment,
    customer_type,
    COUNT(*) AS total_bookings,
    ROUND(AVG(adr), 2) AS avg_daily_rate
FROM bookings
GROUP BY market_segment, customer_type
ORDER BY avg_daily_rate DESC;