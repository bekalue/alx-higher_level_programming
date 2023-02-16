-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM tempratures GROUP BY city ORDER BY value DESC;
