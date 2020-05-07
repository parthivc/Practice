# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/FmBgKWNSMG3DJJKdW

CREATE PROCEDURE consecutiveIds()
BEGIN
    SET @new_id := 0;
    SELECT id AS oldId,
           (@new_id := @new_id + 1) AS newId
    FROM itemIds
    ORDER BY newId;
END
