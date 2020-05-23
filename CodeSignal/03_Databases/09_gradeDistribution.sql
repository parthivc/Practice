# Problem Statement: https://app.codesignal.com/arcade/db/always-leave-table-in-order/jxvpRwWSTtmQne5XN

CREATE PROCEDURE gradeDistribution()
BEGIN
    SELECT Name, ID
    from Grades
    WHERE final > Midterm1 / 2 + Midterm2 / 2
       OR final > Midterm1 / 4 + Midterm2 / 4 + final / 2
    ORDER BY SUBSTRING(name, 1, 3), ID;
END
