# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/rABom8ZdzqkSnDsTo

CREATE PROCEDURE recentHires()
BEGIN
    SET @tmp := 0;
    WITH pr AS (SELECT name, @tmp AS new5 FROM
            (SELECT name FROM pr_department
             ORDER BY date_joined DESC
             LIMIT 5) AS p ORDER BY name),
         it AS (SELECT name, (@tmp := @tmp + 1) AS new5 FROM
             (SELECT name FROM it_department
              ORDER BY date_joined DESC
              LIMIT 5) AS i ORDER BY name),
         sales AS (SELECT name, (@tmp := @tmp + 1) AS new5 FROM
             (SELECT name FROM sales_department
              ORDER BY date_joined DESC
              LIMIT 5) AS s ORDER BY name)
    SELECT names FROM (
        SELECT name as names, new5 FROM pr UNION ALL
        SELECT name as names, new5 FROM it UNION ALL
        SELECT name as names, new5 FROM sales
        ORDER BY new5
    ) as n;
END
