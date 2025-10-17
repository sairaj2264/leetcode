# Write your MySQL query statement below


SELECT(SELECT num FROM MyNumbers
GROUP BY num
HAVING count(*)<2
ORDER BY num DESC
LIMIT 1) AS num