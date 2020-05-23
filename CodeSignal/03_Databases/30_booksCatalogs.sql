# Problem Statement: https://app.codesignal.com/arcade/db/specialties/GvJFyTbHdFqWtXTxc

CREATE PROCEDURE booksCatalogs()
BEGIN
    # https://www.w3schools.com/xml/xpath_axes.asp
    SELECT EXTRACTVALUE(xml_doc, '/descendant-or-self::author[1]') AS author
    FROM catalogs
    ORDER BY author;
END