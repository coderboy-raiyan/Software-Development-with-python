use dummydb;

SELECT *
FROM employees
WHERE salary > (
SELECT salary 
FROM employees
WHERE employee_id = 144
)

SELECT *
FROM employees
WHERE department_id = (SELECT department_id 
FROM departments
WHERE department_name = "Marketing"
)