# Write your MySQL query statement below
SELECT
    a.activity_date as day,
    COUNT(DISTINCT a.user_id) as active_users
FROM
    Activity a
WHERE (activity_date > DATE_SUB('2019-07-27', INTERVAL 30 DAY)
    AND
    activity_date <= '2019-07-27')
GROUP BY a.activity_date
