
drop table if exists first.second;
create table first.second as 

select a,b,c
from d 
where  pt = '2021-12-01';

later view 

substr(pt,1,11) as yymmdd



