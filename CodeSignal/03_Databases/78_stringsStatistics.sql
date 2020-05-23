# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/JrJvTsLSDik4CgoCi

CREATE FUNCTION countLetter(letter VARCHAR(1), str VARCHAR(100)) RETURNS INT DETERMINISTIC
BEGIN
    SET @letterCount = 0;
    SET @remainingString = str;

    WHILE LENGTH(@remainingString) > 0 DO
            SET @firstChar = LEFT(@remainingString, 1);
            IF @firstChar = letter THEN SET @letterCount = @letterCount + 1;
            END IF;

            SET @remainingString = RIGHT(@remainingString, LENGTH(@remainingString)-1);
        END WHILE;
    RETURN @letterCount;
END;

CREATE PROCEDURE stringsStatistics()
BEGIN

    /* create temp table, loop through letters a-z, add rows to table */

    CREATE TABLE IF NOT EXISTS letters (
        letter VARCHAR(1)
    );

    SET @ord = 97;
    WHILE @ord < 123 DO
            INSERT INTO letters(letter)
            VALUES (CHAR(@ord));

            SET @ord = @ord + 1;
        END WHILE;

    CREATE TABLE IF NOT EXISTS letter_count (
                                                letter VARCHAR(1),
                                                str VARCHAR(100),
                                                letterCount INT
    );

    INSERT INTO letter_count
    SELECT * FROM
        (SELECT letter, str, countLetter(letter, str) AS letterCount
         FROM letters, strs
         WHERE LOCATE(letters.letter, strs.str) != 0) AS t1;

    CREATE TABLE IF NOT EXISTS occurrences (
                                               ltr VARCHAR(1),
                                               occurrence INT
    );

    INSERT INTO occurrences
    SELECT * FROM
        (SELECT letter AS ltr, COUNT(letter) AS occurrence
         FROM letters, strs
         WHERE LOCATE(letters.letter, strs.str) != 0
         GROUP BY letter) AS t2;


    CREATE TABLE IF NOT EXISTS ans (
                                       letter VARCHAR(1),
                                       total INT,
                                       occurrence INT,
                                       max_occurrence INT,
                                       max_occurrence_reached INT
    );

    INSERT INTO ans
    SELECT letter, total, occurrence, max_occurrence, max_occurrence_reached FROM
        (SELECT letter, total, occurrence
         FROM
             (SELECT letter, SUM(letterCount) AS total
              FROM letter_count
              GROUP BY letter) AS t2
                 JOIN
             occurrences
             ON t2.letter = occurrences.ltr) AS t5
            JOIN
        (SELECT ltr, max_occurrence, COUNT(ltr) AS max_occurrence_reached
         FROM
             (SELECT letter AS ltr, MAX(letterCount) AS max_occurrence
              FROM letter_count
              GROUP BY letter) AS t4
                 JOIN
             letter_count
             ON t4.ltr = letter_count.letter AND t4.max_occurrence = letter_count.letterCount
         GROUP BY ltr) AS t6
        ON t5.letter = t6.ltr
    ORDER BY letter;

    SELECT *
    FROM ans;

    DROP TABLE letters;
    DROP TABLE letter_count;
    DROP TABLE occurrences;
    DROP TABLE ans;

END