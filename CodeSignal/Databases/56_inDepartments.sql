# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/SnzaCqx4fEu783jaR

CREATE PROCEDURE emptyDepartments()
BEGIN
    SELECT d.dep_name
    FROM departments
             AS d
    WHERE NOT EXISTS (
            SELECT * from employees as e WHERE e.department = d.id
        )
    ORDER BY d.id;
END
