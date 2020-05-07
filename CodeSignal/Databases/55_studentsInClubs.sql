# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/EA3usgZLhJ4mQGJQ3

CREATE PROCEDURE studentsInClubs()
SELECT * FROM students
WHERE EXISTS (
              SELECT * FROM clubs where clubs.id = students.club_id
          )
ORDER BY students.id;
