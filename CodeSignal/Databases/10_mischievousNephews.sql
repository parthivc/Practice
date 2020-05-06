# Problem Statement: https://app.codesignal.com/arcade/db/always-leave-table-in-order/aQJquGtwg4rgXwfqH

CREATE PROCEDURE mischievousNephews()
BEGIN
    SELECT WEEKDAY(mischief_date) AS weekday, mischief_date, author, title
    from mischief
    ORDER BY weekday, field(author, "Huey", "Dewey", "Louie"), mischief_date, title;
END