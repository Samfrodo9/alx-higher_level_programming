-- a script that updates the score of Bob to 10 in the table second_table
SELECT score, name FROM second_table WHERE name = "Bob" SET score = 10;
