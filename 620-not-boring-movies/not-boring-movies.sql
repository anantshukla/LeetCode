# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM Cinema
WHERE ID % 2 = 1 AND description <> "boring"
ORDER BY rating DESC