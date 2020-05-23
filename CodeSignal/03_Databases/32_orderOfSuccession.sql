# Problem Statement: https://app.codesignal.com/arcade/db/when-was-it-the-case/QGQGJF96JDN9bgprX

CREATE PROCEDURE orderOfSuccession()
BEGIN
    SELECT CONCAT(IF(gender = 'M', 'King ', 'Queen '), name) AS name
    FROM Successors
    ORDER BY birthday;
END