# Problem Statement: https://app.codesignal.com/arcade/db/specialties/qeMwFWTCDJeReCeZM

CREATE PROCEDURE habitatArea()
BEGIN
    SELECT ST_Area(ST_ConvexHull(ST_GeomFromText(CONCAT("MultiPoint(", GROUP_CONCAT(x, " ", y), ")"))))
               AS area
    FROM places;
END
