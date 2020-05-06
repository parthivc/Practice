# Problem Statement: https://app.codesignal.com/arcade/db/welcome-to-the-table/RXErLMFkXFkM4MpYY

CREATE PROCEDURE projectList()
BEGIN
    SELECT project_name, team_lead, income
    from Projects
    ORDER BY internal_id;
END