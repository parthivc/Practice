# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/RuKPyy3zx6H3h66sG

CREATE PROCEDURE suspectsInvestigation2()
BEGIN
    SELECT id, name, surname
    from Suspect
    WHERE height <= 170
       OR upper(name) NOT LIKE "B%"
       OR upper(surname) NOT LIKE "GRE_N"
    ORDER BY id;
END