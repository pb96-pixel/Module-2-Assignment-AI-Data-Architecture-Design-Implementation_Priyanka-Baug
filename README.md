# FlexiMart Data Architecture Project

**Student Name:** Priyanka Baug  
**Program:** BITSOM  
**Course:** AI Data Architecture – Module 2  
**Date:** January 2026  

---

## Project Overview

This project implements an end-to-end data architecture solution for FlexiMart, covering transactional data ingestion, NoSQL analysis for flexible product catalogs, and a dimensional data warehouse for analytical reporting. The solution demonstrates ETL pipelines, schema design, MongoDB operations, and OLAP-style business analytics.

---

## Repository Structure

fleximart-data-pipeline/
│
├── part1_sql_etl/
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ └── data_quality_report.txt
│
├── part2_nosql/
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
│
├── part3_data_warehouse/
│ ├── star_schema_design.md
│ ├── warehouse_schema.sql
│ ├── warehouse_data.sql
│ └── analytics_queries.sql
│
└── README.md

---

## Technologies Used

- **Python 3.x** (pandas, mysql-connector-python)
- **MySQL 8.0** (Transactional DB & Data Warehouse)
- **MongoDB 6.0** (NoSQL document database)
- **Git & GitHub** for version control

---

## Setup Instructions

### MySQL Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run ETL Pipeline (Part 1)
python part1_sql_etl/etl_pipeline.py

# Run Business Queries (Part 1)
mysql -u root -p fleximart < part1_sql_etl/business_queries.sql

# Run Data Warehouse Schema & Data (Part 3)
mysql -u root -p fleximart_dw < part3_data_warehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3_data_warehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3_data_warehouse/analytics_queries.sql

# **MongoDB Setup (Part 2)**
mongosh < part2_nosql/mongodb_operations.js

# **Key Learnings**
Designed and implemented a complete ETL pipeline with data quality checks.
Understood when NoSQL databases like MongoDB are preferable over relational models.
Built a star schema data warehouse and wrote OLAP-style analytical queries.
Learned how transactional data is transformed into analytical insights.

# **Challenges Faced**
Schema mismatches during ETL – resolved by standardizing data types and cleaning null values.
Foreign key alignment in data warehouse – resolved through careful dimension loading and surrogate key usage.
GitHub structure confusion – resolved by organizing parts into clear, logical folders.
