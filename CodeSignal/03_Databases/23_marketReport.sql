# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/47JJ5SEJHSdLusQeQ

CREATE PROCEDURE marketReport()
BEGIN
    (SELECT country,
            COUNT(*) as competitors
     FROM foreignCompetitors
     GROUP BY country
     ORDER BY country
     LIMIT 1000)
    UNION
    SELECT 'Total:', COUNT(competitor) as competitors
    FROM foreignCompetitors;
END
