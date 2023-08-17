select animal_ins.name, animal_ins.datetime from animal_ins
left outer join animal_outs
on animal_outs.animal_id = animal_ins.animal_id
where animal_outs.datetime is null
order by animal_ins.datetime
limit 3