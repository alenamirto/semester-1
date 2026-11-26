.headers on
.mode column

.tables

---- 1
select * from customers
limit 10;
-- primary key is customer_id

---- 2
select * from drivers
limit 10;
-- primary key is driver_id

---- 3
select * from menu_items
limit 25;
-- primary key is item_id