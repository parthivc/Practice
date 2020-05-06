# Problem Statement: https://app.codesignal.com/arcade/db/group-dishes-by-type/sCBZwoRFQv2TstL9m

CREATE PROCEDURE soccerPlayers()
BEGIN
    SELECT GROUP_CONCAT(first_name, ' ', surname, ' #', player_number
                        ORDER BY player_number SEPARATOR '; ') AS players
    FROM soccer_team;
END
