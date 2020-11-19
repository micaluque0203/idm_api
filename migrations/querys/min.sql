SELECT ip, country, distance, count(*) as count 
FROM users
GROUP BY 1, 2, 3
ORDER BY distance DESC, count DESC;
