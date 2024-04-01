# Write your MySQL query statement below
SELECT w2.id 
FROM Weather w1, Weather w2
-- WHERE w2.id - w1.id = 1 AND w2.temperature > w1.temperature
WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1 AND w2.temperature > w1.temperature