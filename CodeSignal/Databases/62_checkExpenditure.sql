# Problem Statement: https://app.codesignal.com/arcade/db/selecting-what-to-select/YFxqyqvbMtjzPzLmJ

CREATE PROCEDURE checkExpenditure()
BEGIN
    SELECT a.id AS id,
           IF(SUM(e.expenditure_sum) < a.value, 0,
              SUM(e.expenditure_sum) - a.value)
                AS loss
    FROM expenditure_plan AS e,
         allowable_expenditure AS a
    WHERE WEEK(monday_date)
              BETWEEN a.left_bound
              AND a.right_bound
    GROUP BY a.id;
END
