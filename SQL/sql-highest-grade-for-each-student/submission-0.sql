-- Write your query below


with cte as (select student_id, exam_id, score, max(score) over (partition by student_id) as maxsxorescore
from exam_results) 
select student_id, min(exam_id) as exam_id, score from cte 
where score=maxsxorescore
group by student_id,score
