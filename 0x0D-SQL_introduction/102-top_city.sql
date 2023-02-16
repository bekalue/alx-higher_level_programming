-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_tmp FROM tempratures WHERE month = 7 OR 8 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
