/* Below are another set of problems and solutions from the SQL Data Cleaning module from Udacity's SQL for Data Analysis */



-- QUIZ POSITION, STRPOS, SUBSTR

-- 1. Use the accounts table to create first and last name columns that hold the first and last names for the primary_poc. 

select left(primary_poc, position(' ' in primary_poc) -1) as first,
right(primary_poc, length(primary_poc) - position(' ' in primary_poc)) as last
from accounts;



--QUIZ CONCAT

-- 1. Each company in the accounts table wants to create an email address for each primary_poc. 
-- The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.

select concat(
left(primary_poc, position(' ' in primary_poc)-1),
'.',
right(primary_poc, length(primary_poc) - position(' ' in primary_poc)),
'@',
name,
'.com' 
)
from accounts;



/* 3. We would also like to create an initial password, which they will change after their first log in. 
The first password will be the first letter of the primary_poc's first name (lowercase), 
then the last letter of their first name (lowercase), the first letter of their last name (lowercase), 
the last letter of their last name (lowercase), the number of letters in their first name,
the number of letters in their last name, and then the name of the company they are working with, 
all capitalized with no spaces. */

select concat(
lower(left(primary_poc, 1)),
lower(left(right(primary_poc, length(primary_poc) - position(' ' in primary_poc))
,1)),
lower(right(primary_poc, 1)),
position(' ' in primary_poc)-1,
replace(UPPER(name),' ','')
)from accounts;
