-- Computes and filters the average of a group of records
-- in a table in the database
SELECT city, AVG(value) AS avg_temp FROM temperatures
    WHERE month = 7 OR month = 8
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;
