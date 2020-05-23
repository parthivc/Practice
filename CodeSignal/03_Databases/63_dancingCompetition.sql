# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/YPLqWmfgWJDKTjPAw

CREATE PROCEDURE dancingCompetition()
BEGIN
    SELECT i.arbiter_id, i.first_criterion, i.second_criterion, i.third_criterion
    FROM (
             SELECT *, IF(
                                       first_criterion = (SELECT MAX(first_criterion) FROM scores) OR
                                       first_criterion = (SELECT MIN(first_criterion) FROM scores), 1, 0
                           ) + IF(
                                       second_criterion = (SELECT MAX(second_criterion) FROM scores) OR
                                       second_criterion = (SELECT MIN(second_criterion) FROM scores), 1, 0
                           ) + IF(
                                       third_criterion = (SELECT MAX(third_criterion) FROM scores) OR
                                       third_criterion = (SELECT MIN(third_criterion) FROM scores), 1, 0
                           )
                 AS eCount
             FROM scores
             GROUP BY arbiter_id
         ) AS i WHERE i.eCount <= 1;
END
