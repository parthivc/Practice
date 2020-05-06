# Problem Statement: https://app.codesignal.com/arcade/db/join-us-at-the-table/FJsQ38t6MDWXsCuLP

CREATE PROCEDURE localCalendar()
BEGIN
    SELECT e.event_id,
           DATE_FORMAT(
                   DATE_ADD(e.date, INTERVAL s.timeshift MINUTE),
                   IF(s.hours = 24,
                      "%Y-%m-%d %H:%i",
                      "%Y-%m-%d %h:%i %p"))
               AS formatted_date
    FROM events AS e
             INNER JOIN settings AS s
                        ON e.user_id = s.user_id
    ORDER BY event_id;
END
