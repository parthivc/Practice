# Problem Statement: https://app.codesignal.com/arcade/db/table-metamorphoses/Xp7ws6gzW5b8iYF4K

CREATE PROCEDURE officeBranches()
BEGIN
    ALTER TABLE branches ADD FOREIGN KEY (branchtype_id)
        REFERENCES branch_types (id) ON DELETE SET NULL;

    DELETE FROM branch_types WHERE name LIKE '%-outdated';

    SELECT * FROM branches
    ORDER BY branch_id;
END
