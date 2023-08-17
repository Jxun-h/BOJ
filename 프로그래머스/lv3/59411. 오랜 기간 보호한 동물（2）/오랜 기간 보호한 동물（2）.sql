select ANIMAL_INS.animal_id, ANIMAL_INS.name from ANIMAL_INS
left outer join ANIMAL_OUTS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_OUTS.datetime is not null
order by (ANIMAL_OUTS.datetime - ANIMAL_INS.datetime) desc
limit 2