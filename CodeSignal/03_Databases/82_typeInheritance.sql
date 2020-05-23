# Problem Statement: https://app.codesignal.com/arcade/db/a-table-of-desserts/MYQfuC7ngddKw6LRi

CREATE PROCEDURE typeInheritance()
BEGIN
    SET @first := true;
    WHILE row_count() OR @first DO
            SET @first := false;
            UPDATE inheritance a
                JOIN inheritance b
                ON a.base = b.derived
                    AND a.base != "Number"
            SET a.base = b.base;
        END WHILE;

    SELECT var_name,
           type AS var_type
    FROM variables
             INNER JOIN inheritance
                        ON type = derived
    WHERE base = "Number"
    ORDER BY var_name;
END
