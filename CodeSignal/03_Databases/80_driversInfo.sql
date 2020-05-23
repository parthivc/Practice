# Problem Statement: https://app.codesignal.com/arcade/db/a-table-of-desserts/3XR3Mpj4rRmmqSWP6

CREATE PROCEDURE driversInfo()
BEGIN
    CREATE TABLE IF NOT EXISTS Names (
                                         min_date date,
                                         driver_name VARCHAR(20),
                                         NamesInfo VARCHAR(100)
    );

    INSERT INTO Names
    SELECT date,
           driver_name,
           NamesInfo
    FROM (SELECT (MIN(date) - INTERVAL 1 DAY)
                     AS date,
                 driver_name,
                 CONCAT(' Name: ',
                        driver_name,
                        '; number of inspections: ',
                        COUNT(driver_name),
                        '; miles driven: ',
                        SUM(miles_logged))
                     AS NamesInfo
          FROM inspections
          GROUP BY driver_name)
             AS t1;

    CREATE TABLE IF NOT EXISTS Dates (
        inspection_date date,
        driver_name VARCHAR(20),
        InspectionsInfo VARCHAR(100)
    );

    INSERT INTO Dates
    SELECT date,
           driver_name,
           InspectionsInfo
    FROM (SELECT date,
                 driver_name,
                 CONCAT('  date: ',
                        date,
                        '; miles covered: ',
                        miles_logged)
                     AS InspectionsInfo
          FROM inspections)
             AS t3;

    SELECT *
    FROM (SELECT CONCAT(' Total miles driven by all drivers combined: ',
                        SUM(miles_logged))
                     AS summary
          FROM inspections)
             AS t3
    UNION (SELECT info
           FROM (SELECT *
                 FROM (SELECT min_date
                                  AS date,
                              driver_name,
                              NamesInfo
                                  AS info
                       FROM Names)
                          AS t1
                 UNION (SELECT inspection_date
                                   AS date,
                               driver_name,
                               InspectionsInfo
                                   AS info
                        FROM Dates)
                 ORDER BY driver_name,
                          date)
                    AS t2);
    DROP TABLE Names;
    DROP TABLE Dates;
END
