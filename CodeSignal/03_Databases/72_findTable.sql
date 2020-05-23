# Problem Statement: https://app.codesignal.com/arcade/db/exotic-dishes/qwgoYcGh7SKipb5D3

CREATE PROCEDURE findTable()
BEGIN
    SELECT TABLE_NAME AS tab_name,
           COLUMN_NAME AS col_name,
           DATA_TYPE AS data_type
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'ri_db'
      AND TABLE_NAME LIKE 'e%s'
    ORDER BY tab_name,
             col_name;
END
