/* Write your PL/SQL query statement below */

SELECT a.name, SUM(b.amount)AS balance FROM Users a INNER JOIN Transactions b ON a.account = b.account 
HAVING SUM(b.amount) > 10000;
GROUP BY a.name;

