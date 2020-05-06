# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/mnchRmYiwiJLytZJY

CREATE PROCEDURE securityBreach()
BEGIN
    SELECT first_name, second_name, attribute
    from users
    WHERE attribute LIKE BINARY CONCAT('_%\%', first_name, '\_', second_name, '\%%');
END