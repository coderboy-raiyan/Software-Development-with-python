use dummydb;


WITH AVGIT AS 
(
    SELECT AVG(salary) AS SAL1
	FROM employees
	WHERE department_id = 60
),
MAXIT AS (
    SELECT MAX(salary)	SAL2
    FROM employees
    WHERE department_id = 20
)
SELECT *
FROM employees
WHERE salary > (SELECT SAL1 FROM AVGIT) and salary < (SELECT SAL2 FROM MAXIT)