SELECT
brand_name, avg_price, product_count
FROM products
group by brand_name
having avg(prduct_price) < 200
and count(distinct(product_id)) <= 5
;

-- Netflix example -- 
create table fact_deliveries(
	delivery_id character(30) not null,
	delivery_date date not null,
	delivery_status character(30) not null,
	order_type character(30) not null,
	total_amount float not null,
	merchant_id character(30) not null,
	merchant_rating float,
	consumer_id character(30),
    city_id character(30),
    city_name character(30)

);

INSERT INTO fact_deliveries(delivery_id, delivery_date, delivery_status, order_type,
                           total_amount, merchant_id, merchant_rating, consumer_id, city_id,
                           city_name)
VALUES
('D1', '2021-01-01', 'Placed', 'Delivery', 100.0, 'M1', null, 'C1', 'city1', 'San Francisco'),
('D2', '2021-01-02', 'Placed', 'Pickup', 50.0, 'M2', 4.5, 'C2', 'city2', 'Los Angeles'),
('D1', '2021-01-01', 'Completed', 'Delivery', 100.0, 'M1', 2.5, 'C1', 'city1', 'San Francisco'),
('D2', '2021-01-02', 'Cancelled', 'Pickup', 50.0, 'M2', 4.5, 'C2', 'city2', 'Los Angeles'),
('D3', '2021-02-02', 'Placed', 'Pickup', 150.0, 'M1', null, 'C1', 'city2', 'Los Angeles')

;

select a.delivery_date, a.orders_count,

lag(a.orders_count, 1) over (order by a.delivery_date) as lag_orders
from (
select delivery_date, count(delivery_id) as orders_count from fact_deliveries where delivery_status <> 'Cancelled' group by 1) as a;


select city_name,
delivery_date,
count(delivery_id)
from fact_deliveries
group by 1, 2;

select a.merchant_id from
(select merchant_id, avg(merchant_rating) as avg_rating
from fact_deliveries
where merchant_rating is not null
group by merchant_id
) as a ;

with cte_rankking as
(select a.merchant_id as merchant,
rank() over (order by a.avg_rating desc) as ranking
 from (select merchant_id, avg(merchant_rating) as avg_rating
from fact_deliveries
where merchant_rating is not null
group by merchant_id
) as a)
select merchant, ranking from cte_rankking
where ranking = 1;

select b.merch, b.city from
(select a.merchant_id as merch, a.city_name as city,
row_number() over (order by a.rating) as ranking from
(select merchant_id, city_name,avg(merchant_rating) as rating
from fact_deliveries
where merchant_rating is not null
group by merchant_id, city_name) as a) as b
where b.ranking = 1;

select b.merch as merchant
from
(select a.merchant_id as merch,
row_number() over (order by a.placed_orders desc) as placed_rank
from
(select merchant_id, count(merchant_id) as placed_orders
from fact_deliveries
where delivery_status = 'Placed'
group by merchant_id) as a) as b
where b.placed_rank = 1;

select merchant_id, consumer_id, count(delivery_id) deliveries
from fact_deliveries
group by merchant_id, consumer_id
having deliveries >= 3;

