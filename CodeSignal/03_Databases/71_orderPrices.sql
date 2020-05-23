# Problem Statement: https://app.codesignal.com/arcade/db/express-your-creativity/LhRfNbgyBKM3KKBp9

DROP FUNCTION IF EXISTS get_total;
CREATE FUNCTION get_total(items VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
    SET @total = 0;
    SET @items = CONCAT(items, ';');

    WHILE LOCATE(';', @items) != 0 DO

            SET @currentItem = SUBSTRING(@items FROM 1 FOR LOCATE(';', @items) - 1);
            SET @total = @total + (SELECT price FROM item_prices WHERE id = @currentItem);

            SET @items = SUBSTRING(@items, LOCATE(';', @items) + 1);

        END WHILE;

    RETURN @total;
END;

CREATE PROCEDURE orderPrices()
BEGIN
    SELECT id, buyer, get_total(items) AS total_price
    FROM orders
    ORDER BY id;
END;
