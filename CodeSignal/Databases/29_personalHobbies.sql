# Problem Statement: https://app.codesignal.com/arcade/db/specialties/Kux26wwi4vNpbJhno

CREATE PROCEDURE personalHobbies()
BEGIN
    SELECT name
    FROM people_hobbies
    WHERE hobbies LIKE '%reading%' AND hobbies LIKE '%sports%';
END
