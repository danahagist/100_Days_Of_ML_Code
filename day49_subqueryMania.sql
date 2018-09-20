/* 
Below are a number of subquery problems based on the ERD at the following link: 
https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a0e2796_screen-shot-2017-11-16-at-3.54.06-pm/screen-shot-2017-11-16-at-3.54.06-pm.png
*/

---------------------------- PROBLEMS AND SOLUTIONS ----------------------------------

/*
1. Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
*/
select bill_per_rep.rep_name, bill_per_rep.region, bill_per_rep.total_amt
from
(
select s.name as rep_name, r.name as region, sum(total_amt_usd) as total_amt
from region r
join sales_reps s 
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id
group by s.name, r.name) bill_per_rep
join
(
select region, max(total_amt) as max_amt
from
(
select s.name as rep_name, r.name as region, sum(total_amt_usd) as total_amt
from region r
join sales_reps s 
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id
group by s.name, r.name
) a
group by region
) max_per_region
on max_per_region.max_amt = bill_per_rep.total_amt;



/*
1a. Using WITH Clause, provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
*/
with max_per_region as
(
select region, max(total_amt) as max_amt
from
(
select s.name as rep_name, r.name as region, sum(total_amt_usd) as total_amt
from region r
join sales_reps s 
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id
group by s.name, r.name
) a
group by region
),

bill_per_rep as
(
select s.name as rep_name, r.name as region, sum(total_amt_usd) as total_amt
from region r
join sales_reps s 
on s.region_id = r.id
join accounts a
on a.sales_rep_id = s.id
join orders o
on o.account_id = a.id
group by s.name, r.name
)

select bill_per_rep.rep_name, bill_per_rep.region, bill_per_rep.total_amt
from bill_per_rep
join max_per_region 
on max_per_region.max_amt = bill_per_rep.total_amt;



/*
3. For the name of the account that purchased the most (in total over their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases? 
*/
select count(*) from
(
select a.name as acct_name, sum(o.total) as total_q
from accounts a
join orders o
on o.account_id = a.id
group by a.name
having sum(o.total) >
(
	select total_q
	from
		(
		select a.name as acct_name, 			 		 
    sum(o.standard_qty) as stand_q,
    sum(o.total) as total_q
		from accounts a
		join orders o
		on o.account_id = a.id
		group by a.name
        order by 2 desc
        limit 1) a
)
)count_accts;



/*
5. What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?
*/
select round(avg(total_amt),2)
from
(
	select a.name as acct_name, 			 		sum(o.total_amt_usd) as total_amt
	from accounts a
	join orders o
	on o.account_id = a.id
	group by 1
	order by 2 desc
	limit 10
) largest_accts; 
