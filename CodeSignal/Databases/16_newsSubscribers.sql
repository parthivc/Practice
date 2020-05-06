# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/qLGqhPwQtsrKRzEgv

CREATE PROCEDURE newsSubscribers()
BEGIN
    SELECT subscriber from full_year WHERE INSTR(newspaper, 'Daily')
    UNION
    SELECT subscriber from half_year WHERE INSTR(newspaper, 'Daily')
    ORDER BY subscriber;
END
