# Problem Statement: https://app.codesignal.com/arcade/db/join-us-at-the-table/zoJksWsAGX8NiimFN

CREATE PROCEDURE companyEmployees()
BEGIN
    SELECT dep_name, emp_name
    FROM departments
             CROSS JOIN employees
    ORDER BY dep_name, emp_name;
END
