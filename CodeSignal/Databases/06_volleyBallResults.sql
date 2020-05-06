# Problem Statement: https://app.codesignal.com/arcade/db/always-leave-table-in-order/r34RHt96RkDvPX6gz

CREATE PROCEDURE volleyballResults()
BEGIN
    SELECT *
    from results
    ORDER BY wins;
END