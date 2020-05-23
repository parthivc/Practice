# Problem Statement: https://app.codesignal.com/arcade/db/between-join-and-select/jvZQqfXT3daij9RQo

CREATE PROCEDURE bugsInComponent()
BEGIN
    SELECT bug_title,
           component_title,
           bugs_in_component
    FROM (SELECT t3.component_id,
                 bug_num,
                 bugs_in_component,
                 component_title
          FROM (SELECT component_id,
                       bugs_in_component,
                       title
                           AS component_title
                FROM (SELECT *
                      FROM (SELECT component_id,
                                   COUNT(bug_num)
                                       AS bugs_in_component
                            FROM BugComponent
                            GROUP BY component_id) AS t1) AS t2
                         JOIN Component
                              ON Component.id = t2.component_id) AS t3
                   JOIN BugComponent
                        ON t3.component_id = BugComponent.component_id) AS t4
             JOIN (SELECT bug_num,
                          title
                              AS bug_title
                   FROM (SELECT bug_num,
                                COUNT(component_id)
                                    AS compCount
                         FROM BugComponent
                         GROUP BY bug_num
                         HAVING compCount > 1) AS t3
                            JOIN Bug
                                 ON Bug.num = t3.bug_num) AS t5
                  ON t5.bug_num = t4.bug_num
    ORDER BY bugs_in_component DESC,
             component_id,
             t4.bug_num;
END
