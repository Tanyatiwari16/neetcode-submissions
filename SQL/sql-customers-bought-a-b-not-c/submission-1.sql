-- Write your query below


-- select customer_id, customer_name
-- left join orders on
-- customers_id.customer_id = orders.customer_id
-- where orders.customer_id

-- select 
-- case when product_name = 'A' then 1
-- case when product_name = 'B' then 1

select customer_id,customer_name from customers where customer_id not in (select distinct(customer_id) from orders where product_name ='C') and customer_id in (select distinct(customer_id) from orders where product_name ='A') and customer_id in (select distinct(customer_id) from orders where product_name ='B') order by customer_name