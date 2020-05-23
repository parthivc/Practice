# Problem Statement: https://app.codesignal.com/arcade/db/a-table-of-desserts/Yd8P4ebwe2RQJFxeo

CREATE FUNCTION RomanToArabic(number VARCHAR(50)) RETURNS INT DETERMINISTIC
BEGIN
    /* store a total, set it to zero (also store a LSNV (last seen numeral value), set it to zero)
       start from the rightmost roman numeral
           get its numeral value -- store it in CNV
           if CNV < LSNV:
               add its negation to the total
           else
               add it to the total
           LSNV = CNV
       return the total
    */

    SET @total = 0;
    SET @LSNV = 0;
    SET @remainingString = number;

    WHILE LENGTH(@remainingString) > 0 DO
            SET @CNV = (SELECT Value FROM RomanNumerals WHERE Symbol = RIGHT(@remainingString, 1));
            IF @CNV < @LSNV THEN SET @total = @total - @CNV;
            ELSE SET @total = @total + @CNV;
            END IF;
            SET @LSNV = @CNV;
            SET @remainingString = LEFT(@remainingString, LENGTH(@remainingString)-1);
        END WHILE;

    RETURN @total;

END;


CREATE PROCEDURE sortBookChapters()
BEGIN

    /* write a function */
/* parse from right to left */

    CREATE TABLE IF NOT EXISTS RomanNumerals (
                                                 Symbol VARCHAR(1),
                                                 Value INT
    );

    INSERT INTO RomanNumerals (Symbol, Value)
    VALUES
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000);


    SELECT chapter_name
    FROM
        (SELECT chapter_name,
                chapter_number AS chapter_number_roman,
                RomanToArabic(chapter_number) AS chapter_number_arabic
         FROM book_chapters
         ORDER BY chapter_number_arabic) AS t1;



    DROP TABLE RomanNumerals;
END
