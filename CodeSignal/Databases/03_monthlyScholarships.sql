# Problem Statement: https://app.codesignal.com/arcade/db/welcome-to-the-table/6eMusSHbdjavds7Cq

CREATE PROCEDURE monthlyScholarships()
BEGIN
    SELECT id, scholarship / 12 "scholarship"
    from scholarships;
END