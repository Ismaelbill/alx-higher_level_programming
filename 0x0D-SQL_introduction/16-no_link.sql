-- ists all records of the table second_table of the database hbtn_0c_0
DELETE FROM second_table WHERE name = "George";
INSERT INTO second_table VALUES (5, "Aria", 18);
INSERT INTO second_table VALUES (6, "Aria", 12);
SELECT score, name FROM second_table ORDER BY score DESC;
