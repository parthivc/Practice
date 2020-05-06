# Problem Statement: https://app.codesignal.com/arcade/db/would-you-like-the-second-meal/L3FekSnxCGMpK34bd

CREATE PROCEDURE suspectsInvestigation()
BEGIN
    SELECT id, name, surname
    from Suspect
    WHERE height <= 170
      AND upper(name) LIKE "B%"
      AND upper(surname) LIKE "GRE_N";
END