SELECT
    arrival_date_month,
    COUNT(*) AS total_bookings,
    ROUND(AVG(adr), 2) AS avg_daily_rate
FROM bookings
GROUP BY arrival_date_month
ORDER BY total_bookings DESC;