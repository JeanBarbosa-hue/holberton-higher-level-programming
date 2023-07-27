-- script that lists all records of the table

-- satabase hbtn_0c_0 in your MySQL server

SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
    AND name != ''
ORDER BY score DESC;
