# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/W9abjqqFan2Y5NGwg

CREATE PROCEDURE unluckyEmployees()
BEGIN
    SET @rowNum = 0;
    SELECT dep_name,
           emp_number,
           total_salary
    FROM (SELECT Department.name dep_name,
                 IFNULL(COUNT(Employee.id), 0) emp_number,
                 IFNULL(SUM(Employee.salary), 0) total_salary
          FROM Department
                   LEFT JOIN Employee
                             ON Department.id = Employee.department
          GROUP BY Department.name
          HAVING COUNT(Employee.id) < 6
          ORDER BY IFNULL(SUM(Employee.salary), 0) DESC,
                   IFNULL(COUNT(Employee.id), 0) DESC,
                   Department.id
         ) tmp
    WHERE MOD((@rowNum:=@rowNum + 1), 2) <> 0;
END
