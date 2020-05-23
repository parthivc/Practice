# Problem Statement: https://app.codesignal.com/arcade/db/time-river-revisited/a9iNFQxHGDdh8r8Fi

CREATE PROCEDURE importantEvents()
BEGIN
    SELECT id, name, event_date, participants
    FROM events
    ORDER BY WEEKDAY(event_date),
             participants DESC;
END