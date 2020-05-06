# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/PPNoC7RpXJPGQcqi2

CREATE PROCEDURE movieDirectors()
BEGIN
    SELECT director
    FROM moviesInfo
    WHERE year > 2000
    GROUP BY director
    HAVING SUM(oscars) > 2
    ORDER BY director;
END
