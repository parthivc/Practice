# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/gttNbwKXyN9i8nvYD

CREATE PROCEDURE filmLibrary()
BEGIN
    SELECT starring_actors.actor,
           age
    FROM (movies JOIN
        starring_actors
        ON movies.movie = starring_actors.movie_name)
             JOIN actor_ages
                  ON starring_actors.actor = actor_ages.actor
    WHERE genre = (SELECT genre
                              AS mostCommonGenre
                   FROM (SELECT genre,
                                COUNT(genre)
                                    AS genreCount
                         FROM movies
                         GROUP BY genre
                         ORDER BY genreCount DESC
                         LIMIT 1)
                            AS MCG)
    ORDER BY age DESC, starring_actors.actor;
END
