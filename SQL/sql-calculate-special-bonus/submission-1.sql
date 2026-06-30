-- Write your query below


select employee_id, 
case when MOD(employee_id,2)=1 and name not like 'M%' then cast(salary as INT)
else 0 
end as bonus
from employees order by employee_id asc
