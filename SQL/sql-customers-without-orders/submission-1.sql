-- Write your query below

-- select name from customers
-- left join orders on customers.id = orders.customer_id
-- where orders.id is Null

 select name from customers where id not in (select customer_id FROM orders)
