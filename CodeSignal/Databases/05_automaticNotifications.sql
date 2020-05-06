# Problem Statement: https://app.codesignal.com/arcade/db/welcome-to-the-table/kaxWej78qgdGHy8mr

CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE role NOT IN ("admin", "premium")
    ORDER BY email;
