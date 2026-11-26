.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- 1
select name from drivers;

-- 2
select name,price from menu_items
where price >10;

-- 3
select name, postcode from restaurants
where postcode like 'LS2%';

-- 4
-- order by doesn't specify asc or desc

-- 5 
-- degree is 3