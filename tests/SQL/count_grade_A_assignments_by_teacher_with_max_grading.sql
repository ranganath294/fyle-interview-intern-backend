-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) 
AS number_of_grade_A
FROM assignments a1
WHERE 
a1.grade = 'A' 
AND 
a1.teacher_id = (
    SELECT a2.teacher_id
    FROM assignments a2
    GROUP BY a2.teacher_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)