# Problem Statement: https://app.codesignal.com/arcade/db/exotic-dishes/Mxv2EhqjsGs3oPkNG

CREATE PROCEDURE queriesExecution()
BEGIN
    SET @output = CONCAT(
            (select GROUP_CONCAT(
                            CONCAT(
                                    'select "',
                                    query_name,
                                    '" query_name, (',
                                    CODE,
                                    ') val')
                            SEPARATOR ' UNION ')
             FROM QUERIES),
            ' ORDER BY 1');
    PREPARE qry FROM @output;
    EXECUTE qry;
END
