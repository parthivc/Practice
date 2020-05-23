# Problem Statement: https://app.codesignal.com/arcade/db/time-for-tricks/wcjiSDNohjXc2tpQM

CREATE PROCEDURE combinationLock()
BEGIN
    SET @combos = 1;
    SELECT @combos := @combos * LENGTH(characters) AS combinations
    FROM discs
    ORDER BY combinations DESC
    LIMIT 1;
END
