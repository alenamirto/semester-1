.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- To see all the tables in a database
.tables

-- To see the attributes belonging to each table
.schema customers 
-- degree is num of attributes

-- And to see a count of the total number of tuples
SELECT COUNT(*) as Cardinality FROM customers; 
-- 7, 180 (degree, cardinality)
----------------------------------------------------
.schema reviews
SELECT COUNT(*) as Cardinality FROM reviews; 
-- 4, 412

.schema restaurants
SELECT COUNT(*) as Cardinality FROM restaurants; 
-- 5, 30

.schema menu_items
SELECT COUNT(*) as Cardinality FROM menu_items; 
-- 5, 270

-- week1.9/session1/3-degree-cardinality/task.sql
