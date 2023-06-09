
drop table if exists stores;
create table stores(
  id integer,
  name text,
  allowed_alcohol boolean
  ); 

insert into stores values (1,'Gettar', 1);
insert into stores values (2, 'Waysafe', 0); 

drop table if exists products;
create table products (
  id integer, 
  name text,
  upc text,
  created_at_date
  ); 

insert into products values (1,'Apple', '123', '2018-01-01'); 
insert into products values (2,'Banana', '456', '2018-01-02'); 
insert into products values (3,'Grapes', '789', '2018-01-03');
insert into products values (4,'Golden Banana', '456', '2018-02-04'); 
insert into products values (5,'Bouquet Flowers', '9213123', '2018-02-05');


drop table if exists store_prices;
create table store_prices ( 
  id integer,
  product_id integer,
  store_id integer,
  price numeric 
);

insert into store_prices values (1,3,1,2.59); 
insert into store_prices values (2,2,1,3.32); 
insert into store_prices values (3,4,1,3.59); 
insert into store_prices values (4,3,2,2.34); 
insert into store_prices values (5,1,2,1.56);

drop table if exists order_lines;
create table order_lines ( 
  id integer,
  product_id integer,
  store_id integer,
  qty integer,
  line_total numeric 
  );

insert into order_lines values (1,1,2,3,NULL); 
insert into order_lines values (2,2,1,50,NULL); 
insert into order_lines values (3,2,1,1,NULL); 
insert into order_lines values (4,3,2,4,NULL);

select name from stores where allowed_alcohol = 1;
select price, product_id, store_id from store_prices where store_id = 1;
select price, product_id, store_id from store_prices where store_id = 1 order by price desc;
select product_id, max(qty) from order_lines;
