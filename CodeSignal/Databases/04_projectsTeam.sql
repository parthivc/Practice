# Problem Statement: https://app.codesignal.com/arcade/db/welcome-to-the-table/J8JfCzFnr4cPMQgZ6

CREATE PROCEDURE projectsTeam()
BEGIN
    SELECT DISTINCT name
    FROM projectLog
    ORDER BY name;
END