/* Below are a set of problems and solutions from my SQL practice today */


/*Find the total sales in usd for each account. You should include two columns - 
the total sales for each company's orders in usd and the company name.*/

select a.name acct_name, sum(o.total_amt_usd) total_usd
from orders o
join accounts a
on a.id = o.account_id
group by acct_name;


/*Find the total number of times each type of channel from the web_events was used. 
Your final table should have two columns - the channel and the number of times the channel was used.*/

select w.channel, count(*)
from web_events w
group by w.channel;


/*What was the smallest order placed by each account in terms of total usd. 
Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.*/

select a.name acct_name, sum(total_amt_usd) total_usd
from orders o
join accounts a
on o.account_id = a.id
group by acct_name
order by 2;

/* For each account, determine the average amount spent per order on each paper type. 
Your result should have four columns - one for the account name and one for the average amount spent on each paper type. */

select a.name acct_name, avg(standard_qty) avg_strd, avg(gloss_qty) avg_gloss, avg(poster_qty) avg_pstr
from accounts a
join orders o 
on a.id = o.account_id
group by a.name;


/* Determine the number of times a particular channel was used in the web_events table for each region. 
Your final table should have three columns - the region name, the channel, and the number of occurrences. 
Order your table with the highest number of occurrences first. */

select r.name region_name, w.channel, count(*)
from region r
join sales_reps s
on r.id = s.region_id
join accounts a
on a.sales_rep_id = s.id
join web_events w
on a.id = w.account_id
group by r.name, w.channel
order by 3 desc;


/* Use DISTINCT to test if there are any accounts associated with more than one region. */

SELECT DISTINCT s.name rep_name, r.name region_name
FROM accounts a
join sales_reps s
on a.sales_rep_id = s.id
join region r
on r.id = s.region_id
order by 1;


-- Which account has spent the most with us?

select a.name acct_name, sum(total_amt_usd) as total_usd
from orders o
join accounts a
on a.id = o.account_id
group by a.name
order by 2 desc
limit 1;


/* Which accounts used facebook as a channel to contact customers more than 6 times? */

select a.name acct_name, w.channel channel_name, count(*) as total_contacts
from web_events w
join accounts a
on a.id = w.account_id
where w.channel = 'facebook'
group by a.name, w.channel
having count(*) > 6;


/* Which month did Parch & Posey have the greatest sales in terms of total dollars? 
Are all months evenly represented by the dataset? */

select date_part('month',occurred_at) as ord_month, sum(total_amt_usd)
from orders o
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
group by ord_month
order by 2 desc;


/* Which month did Parch & Posey have the greatest sales in terms of total number of orders? 
Are all months evenly represented by the dataset? */

select date_part('month',occurred_at) as ord_month, sum(total) as tot_ord
from orders o
WHERE occurred_at BETWEEN '2014-01-01' AND '2017-01-01'
group by ord_month
order by 2 desc;


/* We would like to understand 3 different levels of customers based on the amount associated with their purchases in 2016 and 2017. 
The top branch includes anyone with a Lifetime Value (total sales of all orders) greater than 200,000 usd. 
The second branch is between 200,000 and 100,000 usd. The lowest branch is anyone under 100,000 usd. 
Provide a table that includes the level associated with each account. 
You should provide the account name, the total sales of all orders for the customer, and the level.
Order with the top spending customers listed first.*/ 

select a.name acct_name, 
sum(o.total_amt_usd) total_spend,
case when sum(o.total_amt_usd) > 200000 
then 'top' 
when sum(o.total_amt_usd) >= 100000 and sum(o.total_amt_usd) <= 200000
then 'middle'
else 'bottom'
end as acct_tier
from accounts a
join orders o
on o.account_id = a.id
where date_part('year',occurred_at) >= 2016
group by a.name
order by 2 desc;
