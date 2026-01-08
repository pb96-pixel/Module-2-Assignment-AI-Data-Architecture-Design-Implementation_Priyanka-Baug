\# Star Schema Design – FlexiMart Data Warehouse



\## Section 1: Schema Overview



\### FACT TABLE: fact\_sales

\*\*Grain:\*\* One row per product per order line item  

\*\*Business Process:\*\* Sales transactions  



\*\*Measures (Numeric Facts):\*\*

\- quantity\_sold: Number of units sold

\- unit\_price: Price per unit at the time of sale

\- discount\_amount: Discount applied on the line item

\- total\_amount: Final sales value (quantity × unit\_price − discount)



\*\*Foreign Keys:\*\*

\- date\_key → dim\_date

\- product\_key → dim\_product

\- customer\_key → dim\_customer



---



\### DIMENSION TABLE: dim\_date

\*\*Purpose:\*\* Enables time-based sales analysis  

\*\*Type:\*\* Conformed dimension  



\*\*Attributes:\*\*

\- date\_key (PK): Surrogate key in YYYYMMDD format

\- full\_date: Actual calendar date

\- day\_of\_week: Name of the weekday

\- day\_of\_month: Day number within the month

\- month: Numeric month (1–12)

\- month\_name: Month name

\- quarter: Quarter (Q1–Q4)

\- year: Calendar year

\- is\_weekend: Indicates weekend vs weekday



---



\### DIMENSION TABLE: dim\_product

\*\*Purpose:\*\* Stores descriptive product attributes  



\*\*Attributes:\*\*

\- product\_key (PK): Surrogate key

\- product\_id: Business product identifier

\- product\_name: Name of the product

\- category: Product category

\- subcategory: Product subcategory

\- unit\_price: Standard unit price



---



\### DIMENSION TABLE: dim\_customer

\*\*Purpose:\*\* Stores customer demographic information  



\*\*Attributes:\*\*

\- customer\_key (PK): Surrogate key

\- customer\_id: Business customer identifier

\- customer\_name: Full name of the customer

\- city: Customer city

\- state: Customer state

\- customer\_segment: Segment classification (Retail, Corporate, etc.)



---



\## Section 2: Design Decisions



The star schema is designed at the transaction line-item level to capture the most granular form of sales data. This granularity enables flexible analysis such as daily sales trends, product-level performance, and customer purchasing behavior. Aggregations such as monthly or yearly sales can be efficiently derived from this detailed fact table.



Surrogate keys are used instead of natural keys to ensure consistency and performance. Business keys such as customer\_id or product\_id may change over time or vary across systems, while surrogate keys provide stable, system-generated identifiers optimized for joins.



This design supports drill-down and roll-up operations by separating numeric measures in the fact table from descriptive attributes in dimension tables. Analysts can drill down from yearly to monthly to daily sales using the date dimension, or roll up sales by category, city, or customer segment without modifying the fact data.



---



\## Section 3: Sample Data Flow



\*\*Source Transaction:\*\*  

Order #101, Customer “John Doe”, Product “Laptop”, Quantity: 2, Unit Price: ₹50,000  



\*\*Data Warehouse Representation:\*\*



\*\*fact\_sales\*\*

