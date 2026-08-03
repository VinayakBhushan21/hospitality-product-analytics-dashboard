SELECT
    country,
    COUNT(*) AS total_bookings
FROM bookings
WHERE country != 'Unknown'
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 15;