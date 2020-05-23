# Problem Statement: https://app.codesignal.com/arcade/db/specialties/nhGPHWsjFoLb3A4AJ

CREATE PROCEDURE interestClub()
    SELECT name
    FROM people_interests
    WHERE interests && interests LIKE '%reading%' AND interests && interests LIKE '%drawing%'
    # WHERE interests & 1 AND interests & 8  # How does this solution work?
    ORDER BY name
