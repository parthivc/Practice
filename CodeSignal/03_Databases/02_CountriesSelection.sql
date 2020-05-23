# Problem Statement: https://app.codesignal.com/arcade/db/welcome-to-the-table/jLeSZGMvaEhSJnEsS

CREATE PROCEDURE countriesSelection()
BEGIN
    SELECT *
    from countries
    WHERE continent = 'Africa';
END
