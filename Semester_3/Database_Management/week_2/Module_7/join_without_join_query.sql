SELECT employees.first_name, departments.department_name
FROM employees, departments
WHERE employees.department_id = departments.department_id