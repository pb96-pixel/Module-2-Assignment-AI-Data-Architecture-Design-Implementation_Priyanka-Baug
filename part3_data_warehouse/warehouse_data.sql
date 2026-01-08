INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,false),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,true),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,true),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,true),
(20240125,'2024-01-25','Thursday',25,1,'January','Q1',2024,false),

(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,false),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,true),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,true),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,true),
(20240214,'2024-02-14','Wednesday',14,2,'February','Q1',2024,false),
(20240220,'2024-02-20','Tuesday',20,2,'February','Q1',2024,false);

INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Laptop Pro','Electronics','Laptop',75000),
('P002','Smartphone X','Electronics','Mobile',45000),
('P003','Bluetooth Headphones','Electronics','Audio',3000),
('P004','Office Chair','Furniture','Seating',8000),
('P005','Dining Table','Furniture','Table',25000),
('P006','Sofa Set','Furniture','Living',60000),
('P007','Running Shoes','Footwear','Sports',5000),
('P008','Formal Shoes','Footwear','Formal',7000),
('P009','Sandals','Footwear','Casual',2000),
('P010','Gaming Laptop','Electronics','Laptop',95000),
('P011','Tablet','Electronics','Tablet',35000),
('P012','Bookshelf','Furniture','Storage',12000),
('P013','Recliner','Furniture','Seating',40000),
('P014','Sneakers','Footwear','Casual',4500),
('P015','Wireless Mouse','Electronics','Accessory',1500);

INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Mumbai','Maharashtra','Retail'),
('C002','Priya Patel','Ahmedabad','Gujarat','Retail'),
('C003','Amit Verma','Delhi','Delhi','Corporate'),
('C004','Sneha Iyer','Chennai','Tamil Nadu','Retail'),
('C005','Karan Singh','Mumbai','Maharashtra','Corporate'),
('C006','Neha Gupta','Delhi','Delhi','Retail'),
('C007','Rohit Mehta','Ahmedabad','Gujarat','Corporate'),
('C008','Anjali Rao','Chennai','Tamil Nadu','Retail'),
('C009','Vikas Jain','Mumbai','Maharashtra','Retail'),
('C010','Pooja Nair','Chennai','Tamil Nadu','Corporate'),
('C011','Suresh Kumar','Delhi','Delhi','Retail'),
('C012','Meena Shah','Ahmedabad','Gujarat','Retail');

INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240115,1,1,2,75000,5000,145000),
(20240120,2,2,1,45000,0,45000),
(20240125,3,3,3,3000,0,9000),
(20240203,4,4,1,8000,500,7500),
(20240210,5,5,2,25000,2000,48000),
(20240214,6,6,1,60000,5000,55000),
(20240220,7,7,4,5000,0,20000),
(20240106,8,8,2,7000,0,14000),
(20240107,9,9,3,2000,0,6000),
(20240204,10,10,1,95000,10000,85000),
(20240201,11,11,2,35000,0,70000),
(20240101,12,12,1,12000,0,12000);