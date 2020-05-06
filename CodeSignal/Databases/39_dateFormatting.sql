# Problem Statement: https://app.codesignal.com/arcade/db/time-river-revisited/kDhEa99vsWN5apGt8

CREATE PROCEDURE dateFormatting()
BEGIN
    SELECT DATE_FORMAT(date_str, "%Y-%m-%d") AS date_iso
    FROM documents
    ORDER BY id;
END
