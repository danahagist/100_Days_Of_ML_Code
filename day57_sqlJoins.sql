/*Provide a table that provides the region for each sales_rep along with their associated accounts. 
Your final table should include three columns: 
the region name, the sales rep name, and the account name. 
Sort the accounts alphabetically (A-Z) according to account name.*/

SELECT DISTINCT R.NAME REGION_NAME, S.NAME SALES_REP_NAME, A.NAME ACCT_NAME
FROM REGION R
JOIN SALES_REPS S
ON R.ID = S.REGION_ID
JOIN ACCOUNTS A
ON R.ID = S.REGION_ID
ORDER BY 3;


/*Provide a table that provides the region for each sales_rep along with their associated accounts. 
This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. 
Your final table should include three columns: the region name, the sales rep name, and the account name. 
Sort the accounts alphabetically (A-Z) according to account name. */

SELECT REGION.NAME RN, SALES_REPS.NAME SRN, ACCOUNTS.NAME AN 
FROM REGION 
JOIN SALES_REPS ON  REGION.ID=SALES_REPS.REGION_ID  
LEFT JOIN ACCOUNTS ON ACCOUNTS.SALES_REP_ID = SALES_REPS.ID 
WHERE UPPER(REGION.NAME) = 'MIDWEST'
AND UPPER(SALES_REPS.NAME) LIKE 'S%'
ORDER BY AN;


/*Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) 
 for the order. However, you should only provide the results if the standard order quantity exceeds 100. 
Your final table should have 3 columns: region name, account name, and unit price. 
In order to avoid a division by zero error, adding .01 to the denominator here is helpful total_amt_usd/(total+0.01). */

SELECT R.NAME REGION_NAME, A.NAME ACCT_NAME, (O.TOTAL_AMT_USD/(O.TOTAL+.01)) UNIT_PRICE
FROM ORDERS O
JOIN ACCOUNTS A ON O.ACCOUNT_ID = A.ID
AND O.STANDARD_QTY > 100
JOIN SALES_REPS S ON A.SALES_REP_ID = S.ID
JOIN REGION R ON S.REGION_ID = R.ID;


/* Provide the name for each region for every order, as well as the account name and the unit price they paid (total_amt_usd/total) 
for the order. However, you should only provide the results if the standard order quantity exceeds 100 
and the poster order quantity exceeds 50. Your final table should have 3 columns: region name, account name, and unit price. 
Sort for the largest unit price first. 
In order to avoid a division by zero error, adding .01 to the denominator here is helpful (total_amt_usd/(total+0.01).  */

SELECT R.NAME REGION_NAME, A.NAME ACCT_NAME, (O.TOTAL_AMT_USD/(O.TOTAL+.01)) UNIT_PRICE
FROM ORDERS O
JOIN ACCOUNTS A ON O.ACCOUNT_ID = A.ID
AND O.STANDARD_QTY > 100
AND  O.POSTER_QTY > 50                                  
JOIN SALES_REPS S ON A.SALES_REP_ID = S.ID
JOIN REGION R ON S.REGION_ID = R.ID
ORDER BY UNIT_PRICE DESC;


/* Find all the orders that occurred in 2015. Your final table should have 4 columns: 
occurred_at, account name, order total, and order total_amt_usd.  */

SELECT O.OCCURRED_AT, A.NAME ACCT_NAME, O.TOTAL, O.TOTAL_AMT_USD
FROM ORDERS O
JOIN ACCOUNTS A ON O.ACCOUNT_ID = A.ID
where OCCURRED_AT BETWEEN '2015-01-01' AND '2015-12-31'
order by occurred_at;
