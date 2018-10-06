/* Below are a list of problems and solutions from Udacity's SQL for Data Analysis course */


/* There is much debate about how much the name (or even the first letter of a company name) matters. 
Use the accounts table to pull the first letter of each company name
to see the distribution of company names that begin with each letter (or number). */

SELECT LEFT(NAME,1), COUNT(*)
FROM ACCOUNTS
GROUP BY LEFT(NAME,1)
ORDER BY 2 DESC;


/* Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, 
 and what percent start with anything else?  */

SELECT SUM(PROPORTION) AS VOWEL_PROP, 1-SUM(PROPORTION) AS OTHER_PROP FROM
(
  SELECT LEFT(NAME,1) FIRST_LET, COUNT(*) LET_COUNT, (SELECT COUNT(DISTINCT NAME) FROM ACCOUNTS) TOT_COUNT, 
  CAST(COUNT(*) AS FLOAT)/CAST((SELECT COUNT(DISTINCT NAME) 
  FROM ACCOUNTS) AS FLOAT
) PROPORTIONS
FROM ACCOUNTS
WHERE UPPER(LEFT(NAME,1)) IN ('A','E','I','O','U')
GROUP BY LEFT(NAME,1)
ORDER BY 2 DESC) PROPS;


/* Use the sales_reps table to create first and last name columns that hold the first and last names for every rep name. */

SELECT NAME, 
LEFT(NAME,POSITION(' ' IN NAME)) FIRST_NAME,
RIGHT(NAME,LENGTH(NAME)-POSITION(' ' IN NAME)) LAST_NAME                       
FROM SALES_REPS;

                                 
/* Each company in the accounts table wants to create an email address for each primary_poc. 
The email address should be the first name of the primary_poc . last name primary_poc @ company name .com. 
Also, remove all spaces in the account name */ 

select lower(
            replace(
                    concat(left(primary_poc,position(' ' in primary_poc)),
                    '.', 
                    right(primary_poc,length(primary_poc) - position(' ' in primary_poc)),
                    '@',
                    name,
                    '.com'),
             ' ','')
             ) 
from accounts;


/* Create a running total of standard_amt_usd (in the orders table) over order time, 
and date truncate occurred_at by year and partition by that same year-truncated occurred_at variable. 
Your final table should have three columns: One with the amount being added for each row, 
one for the truncated date, and a final column with the running total within each year. */

select date_trunc('year',occurred_at) as occurred_year, standard_amt_usd, sum(standard_amt_usd) 
over (partition by date_trunc('year',occurred_at) 
order by occurred_at) rolling_total 
from orders;                                
                                 
