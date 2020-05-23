# Problem Statement: https://app.codesignal.com/arcade/db/table-metamorphoses/7JdR5aZ8zkTBcyoMd

CREATE PROCEDURE restaurantInfo()
BEGIN
    ALTER TABLE restaurants
        ADD COLUMN description VARCHAR(100)
            DEFAULT("TBD");
    ALTER TABLE restaurants ADD COLUMN active INT DEFAULT(1);

    SELECT * FROM restaurants ORDER BY id;
END
