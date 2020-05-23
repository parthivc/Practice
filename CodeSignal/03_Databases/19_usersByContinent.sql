# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/QnrrbsfdAjNLwkRL2

CREATE PROCEDURE usersByContinent()
BEGIN
    SELECT continent, SUM(users) AS users
    FROM countries
    GROUP BY continent
    ORDER BY users DESC;
END
