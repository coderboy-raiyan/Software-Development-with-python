SELECT emp.name AS "Employee"
FROM employee AS emp
JOIN employee AS mng
ON emp.managerId = mng.id
WHERE emp.salary > mng.salary;