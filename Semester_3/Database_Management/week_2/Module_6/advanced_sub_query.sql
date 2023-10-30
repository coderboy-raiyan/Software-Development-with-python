SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) 
	FROM employees
    WHERE salary < (
		SELECT MAX(salary)
        FROM employees
    )
)


SELECT *
FROM employees AS EMP
WHERE salary > (
	SELECT salary
    FROM employees AS MEG
    WHERE EMP.MANAGER_ID = MEG.MANAGER_ID
)