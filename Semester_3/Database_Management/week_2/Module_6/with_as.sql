use dummydb;

WITH TEMP AS (
	SELECT *
    FROM employees
    LIMIT 5
)
SELECT *
FROM TEMP
