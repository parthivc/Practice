# Problem Statement: https://app.codesignal.com/arcade/db/always-leave-table-in-order/WJ2bsam6YCAqgxFS9

CREATE PROCEDURE contestLeaderboard()
BEGIN
    SELECT name
    from leaderboard
    ORDER BY score DESC LIMIT 5 OFFSET 3;
END