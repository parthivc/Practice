# Problem Statement: https://app.codesignal.com/arcade/db/time-for-tricks/hB9cqdzPpijpE9ttD

CREATE PROCEDURE nullIntern()
BEGIN
    SELECT COUNT(id) as number_of_nulls
    FROM departments
    WHERE description IS NULL
       OR TRIM(UPPER(description)) = 'NULL'
       OR TRIM(UPPER(description)) = 'NIL'
       OR TRIM(UPPER(description)) = '-';
END
