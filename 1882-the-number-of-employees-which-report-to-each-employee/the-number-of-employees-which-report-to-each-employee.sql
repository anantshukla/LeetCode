# Write your MySQL query statement below
SELECT m.employee_id, m.name, COUNT(e.name) AS reports_count, 
ROUND(AVG(e.age)) AS average_age
FROM Employees e INNER JOIN Employees m ON e.reports_to = m.employee_id
GROUP BY m.employee_id
ORDER BY employee_id