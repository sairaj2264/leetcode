# Write your MySQL query statement below
SELECT b.contest_id , round(count(distinct user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
FROM Register B
GROUP BY b.contest_id
ORDER BY percentage DESC, b.contest_id