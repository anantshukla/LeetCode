# Write your MySQL query statement below
SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1
UNION ALL SELECT NULL
ORDER BY num DESC LIMIT 1;

-- SELECT MAX(num) as num FROM MyNumbers WHERE num IN (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1)