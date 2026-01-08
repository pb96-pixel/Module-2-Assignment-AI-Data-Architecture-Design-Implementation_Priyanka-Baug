Section A: Limitations of RDBMS (4 marks - 150 words)

QUESTION: Explain why the current relational database would struggle with:



Products having different attributes (e.g., laptops have RAM/processor, shoes have size/color)

Frequent schema changes when adding new product types

Storing customer reviews as nested data



ANSWER:

Relational databases like MySQL are structured around fixed schemas, which makes them less suitable for highly diverse product catalogs. In FlexiMart’s case, different products have different attributes—laptops may require fields like RAM, processor, and storage, while shoes need size, color, and material. Representing this diversity in an RDBMS requires multiple tables or many nullable columns, leading to inefficient design and complex queries.



Frequent schema changes are another challenge. Each time a new product type is introduced, the database schema must be altered using costly migrations. This increases development overhead and risks downtime in production systems.



Additionally, storing customer reviews as nested data is difficult in relational databases. Reviews must be stored in separate tables and joined with products at query time. As the number of reviews grows, these joins become expensive and negatively impact performance, especially for read-heavy operations such as product listings.



--------------------------------------------------------------

Section B: NoSQL Benefits (4 marks - 150 words)

QUESTION: Explain how MongoDB solves these problems using:



Flexible schema (document structure)

Embedded documents (reviews within products)

Horizontal scalability



ANSWER:

MongoDB addresses these challenges through its flexible, document-based data model. Products can be stored as JSON-like documents where each product contains only the attributes relevant to it. This eliminates the need for rigid schemas and allows different product types to coexist within the same collection.



Embedded documents are another key advantage. Customer reviews can be stored directly inside the product document as an array, enabling fast retrieval without joins. This is especially useful for e-commerce platforms where product details and reviews are frequently accessed together.



MongoDB also supports horizontal scalability through sharding, allowing data to be distributed across multiple servers. This makes it well-suited for handling growing product catalogs and high read/write traffic. Additionally, schema evolution in MongoDB is simple—new fields can be added without modifying existing documents—making it ideal for rapidly evolving business requirements.



--------------------------------------------------------------

Section C: Trade-offs (2 marks - 100 words)

QUESTION: What are two disadvantages of using MongoDB instead of MySQL for this product catalog?



ANSWER:

Despite its advantages, MongoDB has some trade-offs compared to MySQL. First, it provides weaker transactional guarantees. While MongoDB supports transactions, they are more complex and less efficient than traditional ACID transactions in relational databases, making it less suitable for highly transactional systems like payments.



Second, data consistency can be harder to enforce. Since MongoDB allows flexible schemas, improper validation can lead to inconsistent data structures across documents. This requires additional application-level checks to maintain data quality, whereas relational databases enforce consistency more strictly through schema constraints.



