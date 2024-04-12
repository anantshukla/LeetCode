# Write your MySQL query statement below
SELECT user_id, COUNT(user_id) AS followers_count
FROM Followers f
GROUP BY user_id
ORDER BY user_id