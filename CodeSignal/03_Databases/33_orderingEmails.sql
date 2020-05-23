# Problem Statement: https://app.codesignal.com/arcade/db/when-was-it-the-case/KbjWnZy3cpPJxj2st

CREATE PROCEDURE orderingEmails()
BEGIN
    SELECT id, email_title, (IF(size >= POWER(2, 20), CONCAT(TRUNCATE(size / POWER(2, 20), 0), ' Mb'), CONCAT(TRUNCATE(size / POWER(2, 10), 0), ' Kb'))) AS short_size
    FROM emails
    ORDER BY size DESC;
END
