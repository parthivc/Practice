# Problem Statement: https://app.codesignal.com/arcade/db/join-us-at-the-table/zJKgbz4DsDF5oZj3Y

CREATE PROCEDURE scholarshipsDistribution()
BEGIN
    SELECT candidate_id AS student_id
    FROM candidates
    WHERE candidate_id NOT IN
          (SELECT student_id FROM detentions)
    ORDER BY student_id;
END
