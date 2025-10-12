# Write your MySQL query statement below
SELECT a.student_id, a.student_name,b.subject_name, COUNT(c.student_id) AS attended_exams
FROM Students a
CROSS JOIN Subjects b 
LEFT JOIN Examinations c ON b.subject_name = c.subject_name AND a.student_id = c.student_id
GROUP BY a.student_id, a.student_name, b.subject_name
ORDER BY a.student_id, a.student_name, b.subject_name

