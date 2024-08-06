-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(*) AS num_of_graded_assignments_count
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id;