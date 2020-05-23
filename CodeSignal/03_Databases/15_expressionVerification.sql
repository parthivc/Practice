# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/TfCxoCqHXShx7Hhzt

CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT id, a, b, operation, c
    from expressions
    WHERE (operation = '+' AND a + b = c)
       OR (operation = '-' AND a - b = c)
       OR (operation = '/' AND a / b = c)
       OR (operation = '*' AND a * b = c);
END
