# Problem Statement: https://app.codesignal.com/arcade/db/express-your-creativity/uk2oaFYGfFzb4u3XX

DROP PROCEDURE IF EXISTS orderAnalytics;
CREATE PROCEDURE orderAnalytics()
BEGIN

    CREATE OR REPLACE VIEW order_analytics
    AS (SELECT id,
               YEAR(order_date) AS year,
               QUARTER(order_date) AS quarter,
               type,
               quantity * price AS total_price
       FROM orders);

    SELECT *
    FROM order_analytics
    ORDER by id;
END;
