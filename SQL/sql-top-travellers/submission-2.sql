-- Write your query below

with cte as (select user_id, sum(distance) as travelled_distance from rides
group by user_id order by travelled_distance)

select name,
case when travelled_distance is null then  0 
else travelled_distance 
end from users
left join cte on 
users.id = cte.user_id
order by travelled_distance desc, name

