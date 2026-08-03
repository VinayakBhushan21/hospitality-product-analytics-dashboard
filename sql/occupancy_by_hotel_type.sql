SELECT
    hotel,
    COUNT(*) AS total_bookings,
    SUM(is_canceled) AS total_cancellations,
    ROUND(100.0 * SUM(is_canceled) / COUNT(*), 2) AS cancellation_rate_pct,
    ROUND(AVG(total_nights), 2) AS avg_length_of_stay
FROM bookings
GROUP BY hotel;