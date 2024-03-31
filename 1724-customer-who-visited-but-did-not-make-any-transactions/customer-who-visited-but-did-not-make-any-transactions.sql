# Write your MySQL query statement below
-- SELECT v.customer_id, COUNT() as count_no_trans
-- FROM Visits v
-- JOIN Transactions t ON v.visit_id = t.visit_id
-- GROUP BY v.visit_id
-- ORDER BY v.customer_id

SELECT customer_id, COUNT(customer_id) as count_no_trans FROM Visits v WHERE v.visit_id NOT IN (SELECT visit_id FROM Transactions t)
GROUP BY customer_id