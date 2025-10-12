# Write your MySQL query statement below
SELECT a.project_id, IFNULL(ROUND(AVG(b.experience_years),2),0) AS average_years
FROM Project a LEFT JOIN Employee b
ON a.employee_id = b.employee_id
GROUP BY project_id
ORDER BY average_years