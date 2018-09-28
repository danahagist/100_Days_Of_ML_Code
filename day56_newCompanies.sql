/*
--------------------------- PROBLEM ------------------------------------------------
Given the table at https://www.hackerrank.com/challenges/the-company/problem, 
write a query to print the company_code, founder name, total number of lead managers, 
total number of senior managers, total number of managers, and total number of employees. 
Order your output by ascending company_code.
*/

---------------------------- SOLUTION ----------------------------------------------

SELECT C.COMPANY_CODE, C.FOUNDER, COUNT(DISTINCT LM.LEAD_MANAGER_CODE) NUM_LEAD_MGR, COUNT(DISTINCT SM.SENIOR_MANAGER_CODE) NUM_SR_MGR, COUNT(DISTINCT M.MANAGER_CODE) NUM_MGR, COUNT( DISTINCT EMPLOYEE_CODE) NUM_EMP FROM COMPANY C
LEFT JOIN LEAD_MANAGER LM ON C.COMPANY_CODE = LM.COMPANY_CODE
LEFT JOIN SENIOR_MANAGER SM ON LM.LEAD_MANAGER_CODE = SM.LEAD_MANAGER_CODE
LEFT JOIN MANAGER M ON SM.SENIOR_MANAGER_CODE = M.SENIOR_MANAGER_CODE
LEFT JOIN EMPLOYEE E ON M.MANAGER_CODE = E.MANAGER_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER
ORDER BY C.COMPANY_CODE ASC;

--------------------------- END SOLUTION --------------------------------------------
