SELECT name AS "Customers"
FROM customers
LEFT JOIN orders
ON customers.id = orders.customerId
GROUP BY customers.id
HAVING COUNT(orders.id) = 0