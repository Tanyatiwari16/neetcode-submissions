-- Write your query below


with cte as(select customer_id, sum(revenue) as total_revenue from customers
where year=2020 
group by customer_id)
select customer_id from cte
where cte.total_revenue>0
