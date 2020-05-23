# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/qBv2rHiFQNzs7ow5Z

CREATE PROCEDURE freeSeats()
BEGIN
    SELECT flight_id,
           (number_of_seats - taken_seats)
               AS free_seats
    FROM (SELECT flight_id,
                 plane_id
                     AS pid,
                 IF (taken_seats IS NULL, 0, taken_seats)
                     AS taken_seats
          FROM flights
                   LEFT JOIN (SELECT flight_id
                                         AS fid,
                                     COUNT(seat_no)
                                         AS taken_seats
                              FROM purchases
                              GROUP BY flight_id)
              AS t1
                             ON flights.flight_id = t1.fid)
             AS t2
             JOIN planes
                  ON planes.plane_id = t2.pid
    ORDER BY flight_id;
END
