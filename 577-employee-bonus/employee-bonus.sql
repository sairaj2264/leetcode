# Write your MySQL query statement below
SELECT a.name AS name, b.bonus AS bonus FROM 
Employee a LEFT JOIN Bonus b on a.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL