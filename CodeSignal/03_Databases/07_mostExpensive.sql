# Problem Statement: https://app.codesignal.com/arcade/db/always-leave-table-in-order/mcKKnmKK9xEWaFnqP

CREATE PROCEDURE mostExpensive()
BEGIN
    SELECT name
    from Products
    ORDER BY price * quantity DESC, name LIMIT 1;
END
