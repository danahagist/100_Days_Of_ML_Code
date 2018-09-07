/*
TASK:
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
Note: Print NULL when there are no more names corresponding to an occupation.
*/

-- Solution --

select d,p,s,a from                                        
(                                                
-- This subquery assigns a row number to each name within each occupation in alphabetical order
select Name, Occupation, row_number() over(partition by Occupation order by Name) as rn      
from Occupations                                        
)                                                
pivot                                                
(                                                
-- for Occupation creates the necessary columns
--- max(Name) will list out each Name within the occupation
max(Name) for Occupation in ('Doctor' d,'Professor' p,'Singer' s,'Actor' a)            
)  
-- order by rn produces the list of results based on the row number assigned earlier.
order by rn;      
