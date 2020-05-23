# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/NEmMmhyncr4X4ZHbh

CREATE PROCEDURE testCheck()
    SELECT id, IF (given_answer is NULL, "no answer", IF (given_answer = correct_answer, 'correct', 'incorrect')) AS checks
    FROM answers
    ORDER BY id;
