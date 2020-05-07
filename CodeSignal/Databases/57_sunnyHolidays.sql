# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/TTcpS2rcPYsC3HZq2

CREATE PROCEDURE sunnyHolidays()
BEGIN
    SELECT h.holiday_date
               AS ski_date
    FROM holidays
             AS h
    WHERE EXISTS (
                  SELECT * FROM weather as w WHERE w.sunny_date = h.holiday_date
              )
    ORDER BY h.holiday_date;
END
