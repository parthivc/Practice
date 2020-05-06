# Problem Statement: https://app.codesignal.com/arcade/db/join-us-at-the-table/5KqR57uSz9u27KnzP

CREATE PROCEDURE placesOfInterestPairs()
BEGIN
    SELECT s1.name AS place1,
           s2.name AS place2
    FROM sights AS s1,
         sights AS s2
    WHERE ST_DISTANCE(Point(s1.x, s1.y), Point(s2.x, s2.y)) < 5
      AND s1.name < s2.name
    ORDER BY place1, place2;
END
