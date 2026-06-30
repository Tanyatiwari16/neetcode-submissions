-- Write your query below
with cte as(select distinct(sales_id) from orders
left join company
on orders.com_id = company.com_id
where company.name='CRIMSON')
select name from sales_person
where sales_id not in (select sales_id from cte)


-- select name from sales_person
-- where sales_id not in (select distinct(sales_id) from orders
-- left join company
-- on orders.com_id = company.com_id
-- where company.name='CRIMSON')

-- select name from sales_person where sales_id not in cte


