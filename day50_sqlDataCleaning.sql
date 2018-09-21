/* 
Below are a set of problems and solutions from the Udacity "SQL for Data Analysis" course,
in the section devoted to "SQL Data Cleaning."  These expressions are extremely useful for manipulating data.
*/



/* 1. In the accounts table, there is a column holding the website for each company. 
The last three digits specify what type of web address they are using. 
A list of extensions (and pricing) is provided here. 
Pull these extensions and provide how many of each website type exist in the accounts table.*/

select RIGHT(website,3) as domain, count(*)
from accounts
group by domain;



/* 3. Use the accounts table and a CASE statement to create two groups: 
one group of company names that start with a number and a second group of those company names that start with a letter. 
What proportion of company names start with a letter?*/

WITH NUM_COUNT AS
(
SELECT
CASE WHEN LEFT(name,1) in ('0','1','2','3','4','5','6','7','8','9') THEN 1 else 0 END as is_num,
count(*) as counts1
from accounts
WHERE CASE WHEN LEFT(name,1) in ('0','1','2','3','4','5','6','7','8','9') THEN 1 else 0 END = 1
group by is_num
),
LET_COUNT AS
(SELECT
CASE WHEN LEFT(name,1) in ('0','1','2','3','4','5','6','7','8','9') THEN 1 else 0 END as is_num,
count(*) as counts2
from accounts
WHERE CASE WHEN LEFT(name,1) in ('0','1','2','3','4','5','6','7','8','9') THEN 1 else 0 END = 0
group by is_num
)

SELECT LET_COUNT.counts2 / (NUM_COUNT.counts1 + LET_COUNT.counts2)  as proportion from NUM_COUNT, LET_COUNT;




