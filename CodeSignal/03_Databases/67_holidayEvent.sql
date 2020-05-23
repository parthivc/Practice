# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/cWLaGe4qSX7T7d8nf

CREATE PROCEDURE holidayEvent()
BEGIN
    SET @k := 0;
    SELECT DISTINCT buyer_name AS winners
    FROM (SELECT buyer_name, (@k := @k + 1)
        AS num
          FROM purchases) AS x
    WHERE num MOD 4 = 0
    ORDER BY winners;
END
