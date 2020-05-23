# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/p7k9JJ5fqyD6DdFZJ

CREATE PROCEDURE travelDiary()
BEGIN
    SELECT GROUP_CONCAT(DISTINCT country SEPARATOR ';') AS countries
    FROM diary;
END
