/* Below are a set of problems and solutions on SQL Aggregations */


/* Find the total amount of standard_qty paper ordered in the orders table. */

select sum(standard_qty) from orders;


/* Find the total amount spent on standard_amt_usd and gloss_amt_usd paper for each order in the orders table. 
This should give a dollar amount for each order in the table. */

select standard_amt_usd + gloss_amt_usd from orders;


/* When was the earliest order ever placed without using an aggregation function? You only need to return the date. */ 

select occurred_at
from orders
order by 1
limit 1;


/* When did the most recent (latest) web_event occur, without using an aggregation function. */ 

select occurred_at
from web_events
order by 1 desc
limit 1;


/* What is the MEDIAN total_usd spent on all orders? */ 

with half_count as (
select ceiling(count(*))/2 as row_filt from orders), 
sorted_totals as(
select row_number() over (order by total_amt_usd) row_num, total_amt_usd
from orders
order by total_amt_usd)
select * from sorted_totals
where sorted_totals.row_num = (select row_filt from half_count);

