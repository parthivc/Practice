# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/NQ5LyGx2X57AmmJ2G

CREATE PROCEDURE trackingSystem()
BEGIN
    WITH tID AS (SELECT DISTINCT anonymous_id AS id
            FROM tracks ORDER BY anonymous_id
        ),
        tLast AS (SELECT id,
            (SELECT event_name
            FROM tracks
            WHERE anonymous_id = t.id
                AND user_id IS NULL
            ORDER BY received_at DESC LIMIT 1)
            AS event_name FROM tID AS t
        ),
        tFirst AS (SELECT id,
            (SELECT event_name
            FROM tracks
            WHERE anonymous_id = t.id
                AND user_id IS NOT NULL
            ORDER BY received_at LIMIT 1)
            AS event_name FROM tID AS t
        )
    SELECT l.id AS anonym_id, l.event_name AS last_null,
        f.event_name AS first_notnull FROM tFirst AS f, tLast AS l
    WHERE l.id = f.id;
END