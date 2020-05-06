# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/h7GGsvN5tFMx5kytQ

CREATE PROCEDURE countriesInfo()
BEGIN
    SELECT COUNT(name) as 'number',
           AVG(population) as 'average',
           SUM(population) as 'total'
    FROM countries;
END
