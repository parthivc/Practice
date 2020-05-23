# Problem Statement: https://app.codesignal.com/arcade/db/regular-paradise/q9sqF4H4iY9cqEFYd

CREATE PROCEDURE validPhoneNumbers()
BEGIN
    SELECT name, surname, phone_number
    FROM phone_numbers
    WHERE phone_number REGEXP "^(1-|\\(1\\))(\\d{3}-){2}\\d{4}$"
    ORDER BY surname;
END
