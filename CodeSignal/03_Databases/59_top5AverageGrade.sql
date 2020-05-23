# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/R6FGZDgAiwRdGvpkW

CREATE PROCEDURE top5AverageGrade()
BEGIN
    SELECT ROUND(AVG(ag.grade), 2) AS average_grade
    FROM (
             SELECT grade
             FROM students
             ORDER BY grade DESC
             LIMIT 5
         ) AS ag;
END
