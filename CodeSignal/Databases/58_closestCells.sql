# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/MPozuFjnvYoFPh6KW

CREATE PROCEDURE closestCells()
BEGIN
    SELECT p.id AS id1,
           (SELECT id
            FROM positions AS q
            WHERE p.id != q.id
            ORDER BY ST_Distance(Point(p.x, p.y), Point(q.x, q.y))
            LIMIT 1) AS id2
    FROM positions AS p;
END
