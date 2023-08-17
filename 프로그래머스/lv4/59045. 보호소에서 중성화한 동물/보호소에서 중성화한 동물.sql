select animal_ins.animal_id, animal_ins.animal_type, animal_ins.name from animal_ins
left outer join animal_outs
on animal_outs.animal_id = animal_ins.animal_id
where animal_ins.sex_upon_intake like '%Intact%' and not animal_outs.sex_upon_outcome like '%Intact%'
order by animal_ins.animal_id