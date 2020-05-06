# Problem Statement: https://app.codesignal.com/arcade/db/join-us-at-the-table/nmkfbP6qGo63u6vih

CREATE PROCEDURE userCountries()
BEGIN
    SELECT users.id,
           IFNULL(cities.country, "unknown") AS country
    FROM users
             LEFT JOIN cities
                       ON users.city = cities.city
    ORDER BY users.id;
END
