\# FlexiMart Database Schema Documentation



\## 1. Entity–Relationship Description



\### ENTITY: customers

\*\*Purpose:\*\* Stores customer information for the e-commerce platform.



\*\*Attributes:\*\*

\- customer\_id (PK): Unique system-generated identifier for each customer

\- first\_name: Customer’s first name

\- last\_name: Customer’s last name

\- email: Unique email address of the customer

\- phone: Standardized contact number

\- city: Customer’s city

\- registration\_date: Date the customer registered



\*\*Relationships:\*\*

\- One customer can place many orders (1:M relationship with orders table)



---



\### ENTITY: products

\*\*Purpose:\*\* Stores product catalog information.



\*\*Attributes:\*\*

\- product\_id (PK): Unique identifier for each product

\- product\_name: Name of the product

\- category: Product category (standardized)

\- price: Unit price of the product

\- stock\_quantity: Available inventory



\*\*Relationships:\*\*

\- One product can appear in many order\_items (1:M relationship)



---



\### ENTITY: orders

\*\*Purpose:\*\* Stores order-level transaction details.



\*\*Attributes:\*\*

\- order\_id (PK): Unique identifier for each order

\- customer\_id (FK): References customers.customer\_id

\- order\_date: Date the order was placed

\- total\_amount: Total monetary value of the order

\- status: Order status (e.g., Completed, Pending)



\*\*Relationships:\*\*

\- Each order belongs to one customer

\- Each order can have many order\_items



---



\### ENTITY: order\_items

\*\*Purpose:\*\* Stores item-level details for each order.



\*\*Attributes:\*\*

\- order\_item\_id (PK): Unique identifier for each order item

\- order\_id (FK): References orders.order\_id

\- product\_id (FK): References products.product\_id

\- quantity: Number of units ordered

\- unit\_price: Price per unit at time of purchase

\- subtotal: Calculated as quantity × unit\_price



---



\## 2. Normalization Explanation (Third Normal Form)



The FlexiMart database schema is designed in Third Normal Form (3NF) to ensure data integrity, reduce redundancy, and prevent anomalies.



Each table satisfies First Normal Form (1NF) by containing atomic values and unique primary keys. Second Normal Form (2NF) is achieved because all non-key attributes are fully functionally dependent on the entire primary key. For example, in the order\_items table, attributes such as quantity and unit\_price depend on the order\_item\_id, not partially on order\_id or product\_id.



The design satisfies Third Normal Form (3NF) because there are no transitive dependencies. In the orders table, customer-related details such as name or email are not stored; instead, they are maintained in the customers table and referenced via foreign keys. Similarly, product attributes are stored only in the products table.



Functional dependencies are clearly defined:

\- customer\_id → customer attributes

\- product\_id → product attributes

\- order\_id → order attributes



This separation prevents update anomalies (e.g., changing customer email in one place), insert anomalies (e.g., adding products without orders), and delete anomalies (e.g., deleting an order without losing customer data). Overall, the schema ensures consistency, scalability, and efficient data management.



---



\## 3. Sample Data Representation



\### customers

| customer\_id | first\_name | last\_name | email                | city       |

|------------|-----------|----------|----------------------|------------|

| 1          | Rahul     | Sharma   | rahul@gmail.com      | Bangalore  |

| 2          | Priya     | Patel    | priya@yahoo.com      | Mumbai     |



\### products

| product\_id | product\_name | category     | price |

|-----------|--------------|--------------|-------|

| 1         | Smartphone   | Electronics  | 29999 |

| 2         | Headphones   | Electronics  | 1999  |



\### orders

| order\_id | customer\_id | order\_date | total\_amount | status |

|---------|-------------|------------|--------------|--------|

| 1       | 1           | 2023-06-10 | 31998        | Completed |



\### order\_items

| order\_item\_id | order\_id | product\_id | quantity | subtotal |

|--------------|----------|------------|----------|----------|

| 1            | 1        | 1          | 1        | 29999    |

| 2            | 1        | 2          | 1        | 1999     |



