/* Below are a set of problems and solutions for Udacity's SQL for Data Analysis course */



/* For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed? */ 

select r.name reg_name, sum(total_amt_usd) total_usd, count(*) ord_count
from region r
join sales_reps s
on r.id = s.region_id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id
group by r.name
having sum(total_amt_usd)  =
(
  select max(total_usd)
  from
(
  select r.name reg_name, sum(total_amt_usd) total_usd
  from region r
  join sales_reps s
  on r.id = s.region_id
  join accounts a
  on a.sales_rep_id = s.id
  join orders o
  on o.account_id = a.id
  group by r.name) reg_amts);



/* For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel? */ 

select a.name acct_name, we.channel, count(*) event_count
from accounts a
join web_events we
on we.account_id = a.id
where a.name  =
(
  select acct_name
  from
(
    select a.name acct_name, sum(total_amt_usd) total_usd
    from accounts a
    join orders o
    on o.account_id = a.id
    group by a.name
    order by 2 desc
    limit 1
) 
  accts_amts)
group by a.name, we.channel;



/* What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders. */

select avg(avg_usd) total_avg
from
  (
  select a.name acct_name, avg(total_amt_usd) avg_usd
  from accounts a
  join orders o
  on o.account_id = a.id
  group by a.name
  having avg(total_amt_usd) >
    (
    select avg(total_amt_usd) avg_usd
    from orders o
    ) 
) exc_avg;



/* For the region with the largest sales total_amt_usd, how many total orders were placed?
Use a 'WITH' clause for this problem */

with max_usd as
(select r.name reg_name, sum(total_amt_usd) tot
 from orders o
 join accounts a 
 on o.account_id = a.id
 join sales_reps s
 on a.sales_rep_id = s.id
 join region r
 on s.region_id = r.id
 group by r.name
order by 2 desc
limit 1)

select r.name reg_name, count(*)
 from orders o
 join accounts a 
 on o.account_id = a.id
 join sales_reps s
 on a.sales_rep_id = s.id
 join region r
 on s.region_id = r.id
 group by r.name
 having sum(total_amt_usd) = (select tot from max_usd)


