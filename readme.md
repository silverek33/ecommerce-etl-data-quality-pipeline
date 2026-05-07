# E-commerce ETL & Data Quality Pipeline

Automated ETL pipeline built with Python, Pandas and PostgreSQL.

The project demonstrates how raw e-commerce data can be cleaned, transformed, validated and loaded into a PostgreSQL database for analytical use.

## Business Problem

Raw operational data is often not ready for business reporting.  
It may contain duplicated records, missing values, invalid timestamps, inconsistent categories and incorrect financial values.

The goal of this project is to simulate a real-world ETL process where messy e-commerce data is transformed into a clean, validated and analysis-ready database.

## Dataset

This project uses the Brazilian E-Commerce Public Dataset by Olist.

Raw CSV files are not stored in this repository due to file size limitations and data management best practices.

To run the project locally, download the dataset and place the required CSV files in:
```
data/raw/
```
Required files:
```
olist_orders_dataset.csv
olist_customers_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

ETL Pipeline
```
Raw CSV files
      ↓
Dirty data simulation
      ↓
Data transformation
      ↓
Business rule validation
      ↓
Rejected records / Valid records
      ↓
PostgreSQL staging tables
      ↓
Analytical SQL views
```

Key Features
Automated ETL orchestration
Data quality issue simulation
Data cleaning and standardization
Business rule validation
Rejected records handling
PostgreSQL data loading
Analytical SQL views
Modular Python structure
Data Quality Rules

Examples of validation rules used in the project:

order ID cannot be null
customer ID cannot be null
order status must belong to an accepted status list
order purchase date cannot be in the future
payment value cannot be negative
customer state must use a valid two-letter format

Project Structure
```
data/
  raw/
  dirty/
  processed/
  rejected/

src/
  make_dirty_data.py
  transform.py
  validate.py
  load.py
  main.py

sql/
  03_create_views.sql

logs/
reports/
requirements.txt
.env.example
README.md
```
How to Run
Install dependencies:
```
py -m pip install -r requirements.txt
Create PostgreSQL database:
CREATE DATABASE ecommerce_etl;
Create .env file:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_etl
DB_USER=postgres
DB_PASSWORD=your_password
```
Run full pipeline:
```
py src/main.py
PostgreSQL Tables
```
The pipeline loads data into staging tables:
```
stg_orders
stg_customers
stg_payments
stg_order_items
stg_products
stg_sellers
stg_category_translation
Analytical Views
```
The project includes SQL views for business analysis:
```
vw_sales_summary
vw_top_customers
vw_payment_distribution
vw_data_quality_summary
```
Tech Stack

Python
Pandas
PostgreSQL
SQLAlchemy
python-dotenv
SQL
ETL
Data Quality
