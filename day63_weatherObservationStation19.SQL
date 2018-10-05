/*
--------------------- PROBLEM -----------------------------
Consider P1(a,c) and P2(b,d) to be two points on a 2D plane 
where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) 
and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits.
*/

-------------------- SOLUTION -----------------------------

with coords as(
select max(lat_n) max_lat, min(lat_n) min_lat, max(long_w) max_long, min(long_w) min_long
from station) 
select round(power(power(max_lat - min_lat,2)+ power(max_long - min_long,2),.5),4)
from coords;
