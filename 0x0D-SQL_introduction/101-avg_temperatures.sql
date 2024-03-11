-- display average temperatures by city ordered by temp

SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
