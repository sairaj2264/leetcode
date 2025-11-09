# Write your MySQL query statement below
SELECT a.firstName AS firstName, a.lastName AS lastName, b.city, b.state
FROM Person a
LEFT JOIN
Address b 
ON
a.personId = b.personId