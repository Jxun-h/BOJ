set @hour := -1;

select (@hour := @hour + 1) as 'HOUR', 
(
    select count(hour(datetime)) 
    from animal_outs
    where @hour = hour(datetime)
) as 'COUNT'

from animal_outs
where @hour < 23
group by @hour