.headers on
.mode column
-- week1.9/session1/5-challenges/task.sql
-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.
.tables

---- bronze
-- 1
SELECT name FROM drivers;

-- 2
SELECT name, price FROM menu_items;

-- 3
SELECT name FROM restaurants
WHERE cuisine = 'Indian';

-- 4
SELECT COUNT(*) as Cardinality FROM customers; 
-- 180 customers

---- silver
-- 1
SELECT name, price from menu_items
WHERE is_vegetarian = 1 and price <= 8
ORDER BY price ASC;

-- 2
SELECT name, hygiene_rating from restaurants
WHERE hygiene_rating < 4
ORDER BY hygiene_rating ASC;

-- 3
select name, postcode, hygiene_rating from restaurants
where postcode like 'LS6%'
order by hygiene_rating desc;