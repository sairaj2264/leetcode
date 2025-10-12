# Write your MySQL query statement below
SELECT a.id, a.movie, a.description, a.rating FROM Cinema a
WHERE mod(a.id , 2) = 1 AND a.description <>'boring' 
ORDER BY a.rating DESC