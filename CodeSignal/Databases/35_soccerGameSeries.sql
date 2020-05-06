# Problem Statement: https://app.codesignal.com/arcade/db/when-was-it-the-case/CZBMSWZTZCHc4rcFo

CREATE PROCEDURE soccerGameSeries()
BEGIN
    SELECT IF(wins > 0, 1,
              IF(wins < 0, 2,
                 IF(diff > 0, 1,
                    IF(diff < 0, 2,
                       IF(host > 0, 1,
                          IF(host < 0, 2, 0)
                           )
                        )
                     )
                  )
               ) winner
    FROM (
             SELECT
                 SUM(IF(first_team_score > second_team_score, 1, -1)) wins,
                 SUM(first_team_score - second_team_score) diff,
                 SUM(IF(match_host = 2, first_team_score, -second_team_score)) host
             FROM scores
         ) x;
END
