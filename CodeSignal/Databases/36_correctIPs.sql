# Problem Statement: https://app.codesignal.com/arcade/db/regular-paradise/XYXE3mXLuZ243yqmb

CREATE PROCEDURE correctIPs()
BEGIN
    SELECT id, ip
    FROM ips
    WHERE ip REGEXP "\\d\\d\\.\\d|\\.\\d\\d"
      AND IS_IPV4(ip)
    ORDER BY id;
END
