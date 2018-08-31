/*
Task:
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths 
(i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/

SELECT CITY, CITY_LEN FROM
(SELECT CITY, LENGTH(CITY) AS CITY_LEN FROM STATION ORDER BY LENGTH(CITY), CITY) WHERE ROWNUM = 1
UNION
SELECT CITY, CITY_LEN FROM
(SELECT CITY, LENGTH(CITY) AS CITY_LEN FROM STATION ORDER BY LENGTH(CITY) DESC, CITY) WHERE ROWNUM = 1;
