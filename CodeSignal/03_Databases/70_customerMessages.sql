# Problem Statement: https://app.codesignal.com/arcade/db/express-your-creativity/W9KE9psZwJpTeLffw

DROP FUNCTION IF EXISTS response;
CREATE FUNCTION response(name VARCHAR(40)) RETURNS VARCHAR(200) DETERMINISTIC
BEGIN
    SET @fName = LOWER(SUBSTRING_INDEX(name, ' ', 1));
    SET @lName = LOWER(SUBSTRING_INDEX(name, ' ', -1));

    SET @fName = CONCAT(UPPER(LEFT(@fName, 1)),SUBSTRING(@fName, 2));
    SET @lName = CONCAT(UPPER(LEFT(@lName, 1)),SUBSTRING(@lName, 2));

    RETURN CONCAT('Dear ', @fName, ' ', @lName, '! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.');
END;

CREATE PROCEDURE customerMessages()
BEGIN
    SELECT id, name, response(name) AS response
    FROM customers;
END;
