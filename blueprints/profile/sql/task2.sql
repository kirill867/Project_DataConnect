SELECT order_id, date
FROM orders
WHERE '$date1' < date AND date < '$date2'
