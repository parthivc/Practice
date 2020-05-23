# Problem Statement: https://app.codesignal.com/arcade/db/time-river-revisited/G9zoZjTzk6JpJGFbd

CREATE PROCEDURE alarmClocks()
BEGIN
    SET @date := (SELECT input_date FROM userInput);
    SET @year := YEAR(@date);
    DROP TABLE IF EXISTS alarmDates;
    CREATE TABLE alarmDates (alarm_date datetime);
    WHILE YEAR(@date) = @year DO
            INSERT INTO alarmDates(alarm_date)
            SELECT @date;
            SET @date := @date + INTERVAL 7 DAY;
        END WHILE;
    SELECT *
    FROM alarmDates;
END
