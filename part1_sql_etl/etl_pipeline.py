import pandas as pd
import re

print("ETL Pipeline started")

# -----------------------------
# EXTRACT
# -----------------------------
customers_file = "../data/customers_raw.csv"
customers_df = pd.read_csv(customers_file)

raw_count = len(customers_df)
print("Raw customer records:", raw_count)

# -----------------------------
# TRANSFORM
# -----------------------------

# 1. Remove duplicate rows
customers_df = customers_df.drop_duplicates()
duplicates_removed = raw_count - len(customers_df)

# 2. Handle missing emails
customers_df["email"] = customers_df["email"].replace(r"^\s*$", pd.NA, regex=True)
missing_emails_before = customers_df["email"].isna().sum()

# Strategy: drop records with missing email
customers_df = customers_df.dropna(subset=["email"])
missing_emails_removed = missing_emails_before

# 3. Standardize phone numbers to +91-XXXXXXXXXX
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return "+91-" + digits
    elif len(digits) == 12 and digits.startswith("91"):
        return "+91-" + digits[2:]
    else:
        return None

customers_df["phone"] = customers_df["phone"].apply(standardize_phone)

# 4. Standardize registration_date to YYYY-MM-DD
customers_df["registration_date"] = pd.to_datetime(
    customers_df["registration_date"],
    errors="coerce",
    dayfirst=True
)

# Convert NaT to None for MySQL compatibility
customers_df["registration_date"] = customers_df["registration_date"].apply(
    lambda x: x.date() if pd.notnull(x) else None
)

clean_count = len(customers_df)

# -----------------------------
# TRANSFORM SUMMARY
# -----------------------------
print("Duplicates removed:", duplicates_removed)
print("Records removed due to missing email:", missing_emails_removed)
print("Clean customer records:", clean_count)
# -----------------------------
# DATA QUALITY REPORT
# -----------------------------
report_lines = [
    f"Raw customer records: {raw_count}",
    f"Duplicates removed: {duplicates_removed}",
    f"Records removed due to missing email: {missing_emails_removed}",
    f"Clean customer records loaded: {clean_count}"
]

with open("data_quality_report.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")

print("Data quality report generated: data_quality_report.txt")
# =================================================
# PRODUCTS - EXTRACT
# =================================================
products_file = "../data/products_raw.csv"
products_df = pd.read_csv(products_file)

print("\nRaw product records:", len(products_df))
print("Product columns:", list(products_df.columns))


# =================================================
# PRODUCTS - TRANSFORM
# =================================================

# Remove duplicates
products_df = products_df.drop_duplicates()

# Drop records with missing price
products_df = products_df.dropna(subset=["price"])

# Fill missing stock with 0
products_df["stock_quantity"] = products_df["stock_quantity"].fillna(0).astype(int)

# Standardize category names
products_df["category"] = products_df["category"].str.strip().str.title()

clean_products_count = len(products_df)
print("Clean product records:", clean_products_count)
# -----------------------------
# LOAD TO MYSQL (CUSTOMERS)
# -----------------------------
# import mysql.connector
#
# try:
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="GhS1Q2L3$",
#         database="fleximart"
#     )
#
#     cursor = connection.cursor()
#
#     insert_query = """
#         INSERT INTO customers
#         (first_name, last_name, email, phone, city, registration_date)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """
#
#     records_loaded = 0
#
#     for _, row in customers_df.iterrows():
#         cursor.execute(insert_query, (
#             row["first_name"],
#             row["last_name"],
#             row["email"],
#             row["phone"],
#             row["city"],
#             row["registration_date"]
#         ))
#         records_loaded += 1
#
#     connection.commit()
#     print(f"Clean customer records loaded: {records_loaded}")
#
# except mysql.connector.Error as err:
#     print("Error while loading data:", err)
#
# finally:
#     if 'connection' in locals() and connection.is_connected():
#         cursor.close()
#         connection.close()
# =================================================
# SALES - EXTRACT
# =================================================
sales_file = "../data/sales_raw.csv"
sales_df = pd.read_csv(sales_file)

raw_sales_count = len(sales_df)
print("\nRaw sales records:", raw_sales_count)
print("Sales columns:", list(sales_df.columns))
# =================================================
# SALES - TRANSFORM
# =================================================

# Remove duplicate rows
sales_df = sales_df.drop_duplicates()

# Drop rows with missing customer_id or product_id
sales_df = sales_df.dropna(subset=["customer_id", "product_id"])

# Rename transaction_date to order_date (schema alignment)
sales_df = sales_df.rename(columns={"transaction_date": "order_date"})

# Standardize order_date
sales_df["order_date"] = pd.to_datetime(
    sales_df["order_date"],
    errors="coerce",
    dayfirst=True
)

# Drop rows where date could not be parsed
sales_df = sales_df.dropna(subset=["order_date"])

# Ensure numeric types
sales_df["quantity"] = sales_df["quantity"].astype(int)
sales_df["unit_price"] = sales_df["unit_price"].astype(float)

# Calculate subtotal
sales_df["subtotal"] = sales_df["quantity"] * sales_df["unit_price"]

clean_sales_count = len(sales_df)
print("Clean sales records:", clean_sales_count)
# =================================================
# MAP RAW IDS TO DATABASE IDS
# =================================================

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GhS1Q2L3$",
    database="fleximart"
)

cursor = connection.cursor()

# Fetch customer mapping
cursor.execute("SELECT customer_id, email FROM customers")
customer_map = {}

for db_id, email in cursor.fetchall():
    customer_map[email] = db_id

# Fetch product mapping
cursor.execute("SELECT product_id, product_name FROM products")
product_map = {}

for db_id, name in cursor.fetchall():
    product_map[name] = db_id

cursor.close()
connection.close()
# Replace raw customer_id with DB customer_id using email
sales_df["customer_id"] = sales_df["customer_id"].map(
    customers_df.set_index("customer_id")["email"]
).map(customer_map)

# Replace raw product_id with DB product_id using product_name
sales_df["product_id"] = sales_df["product_id"].map(
    products_df.set_index("product_id")["product_name"]
).map(product_map)

# Drop rows where mapping failed
sales_df = sales_df.dropna(subset=["customer_id", "product_id"])

sales_df["customer_id"] = sales_df["customer_id"].astype(int)
sales_df["product_id"] = sales_df["product_id"].astype(int)
# =================================================
# SALES -> ORDERS (CREATE ORDERS DATAFRAME)
# =================================================
orders_df = (
    sales_df
    .groupby(["customer_id", "order_date", "status"], as_index=False)
    .agg(total_amount=("subtotal", "sum"))
)

print("Orders to be created:", len(orders_df))
# =================================================
# LOAD TO MYSQL (ORDERS & ORDER_ITEMS)
# =================================================
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GhS1Q2L3$",
        database="fleximart"
    )

    cursor = connection.cursor()

    # -----------------------------
    # INSERT INTO ORDERS
    # -----------------------------
    order_id_map = {}

    insert_order_query = """
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
    """

    for _, row in orders_df.iterrows():
        cursor.execute(insert_order_query, (
            row["customer_id"],
            row["order_date"],
            row["total_amount"],
            row["status"]
        ))
        order_id_map[(row["customer_id"], row["order_date"])] = cursor.lastrowid

    # -----------------------------
    # INSERT INTO ORDER_ITEMS
    # -----------------------------
    insert_item_query = """
        INSERT INTO order_items
        (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s, %s, %s, %s, %s)
    """

    for _, row in sales_df.iterrows():
        order_id = order_id_map[(row["customer_id"], row["order_date"])]
        cursor.execute(insert_item_query, (
            order_id,
            row["product_id"],
            row["quantity"],
            row["unit_price"],
            row["subtotal"]
        ))

    connection.commit()
    print("Orders and order items loaded successfully")

except mysql.connector.Error as err:
    print("Error loading sales data:", err)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
# -----------------------------
# LOAD TO MYSQL (PRODUCTS)
# -----------------------------
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="GhS1Q2L3$",
        database="fleximart"
    )

    cursor = connection.cursor()

    insert_product_query = """
        INSERT INTO products
        (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """

    products_loaded = 0

    for _, row in products_df.iterrows():
        cursor.execute(insert_product_query, (
            row["product_name"],
            row["category"],
            row["price"],
            row["stock_quantity"]
        ))
        products_loaded += 1

    connection.commit()
    print(f"Clean product records loaded: {products_loaded}")

except mysql.connector.Error as err:
    print("Error while loading products:", err)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
