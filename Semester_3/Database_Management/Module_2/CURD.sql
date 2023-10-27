USE programmingHero;

CREATE TABLE Student(
	Roll CHAR(4) PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

DROP TABLE Student




INSERT INTO Students (Roll, name, email) VALUES (1, "roya", "eoya@");-- 
INSERT INTO Students (Roll, name) VALUES (2, "roya2");

SET sql_safe_updates = 0;
UPDATE Students 
	SET name = "Raiyan"
    WHERE ROLL = 1;
SET sql_safe_updates = 1;


SET sql_safe_updates = 0;
DELETE FROM Students 
WHERE Roll = 2;
SET sql_safe_updates = 1;