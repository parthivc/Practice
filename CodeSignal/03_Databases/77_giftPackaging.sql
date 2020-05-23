# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/mEevFeQL67fZ53fAk

CREATE PROCEDURE giftPackaging()
BEGIN
    SELECT package_type,
           COUNT(id)
               AS number
    FROM (SELECT id,
                 package_type
          FROM (SELECT id,
                       MIN(vol)
                           AS packageVol
                FROM (SELECT id,
                             gift_name,
                             length,
                             width,
                             height,
                             length * width * height
                                 AS volume
                      FROM gifts)
                         AS gfts
                         JOIN (SELECT package_type,
                                      length
                                          AS len,
                                      width
                                          AS wid,
                                      height
                                          AS hgt,
                                      length * width * height
                                          AS vol
                               FROM packages)
                    AS pkgs
                              ON length <= len
                                  AND width <= wid
                                  AND height <= hgt
                                  AND volume <= vol
                GROUP BY id) AS t1
                   JOIN packages
                        ON packageVol = packages.length*packages.width*packages.height)
             AS t2
    GROUP BY package_type
    ORDER BY package_type;
END
