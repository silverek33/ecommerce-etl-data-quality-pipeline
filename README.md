# Ecommerce ETL & Data Quality Pipeline

End-to-end ecommerce data pipeline built with **Python, Pandas, PostgreSQL and Power BI**.

The project demonstrates a complete workflow from raw ecommerce CSV files, through ETL processing, validation and rejected records handling, to PostgreSQL staging tables, SQL analytical views and Power BI reporting.

---

# Business Context

Raw operational data is often not ready for analysis.
It may contain duplicates, missing values, inconsistent formats, invalid timestamps or incorrect financial records.

This project simulates a realistic ecommerce data workflow where raw data is transformed, validated and prepared for business reporting.

The goal was to build a practical data pipeline showing:

* ETL automation
* Data cleaning
* Validation rules
* Rejected records handling
* PostgreSQL loading
* Analytical SQL views
* Power BI reporting
* Data quality monitoring

---

# Pipeline Architecture

```text
Raw CSV Data
    ↓
Dirty Data Simulation
    ↓
Python ETL Pipeline
    ↓
Transformation Layer
    ↓
Validation & Rejected Records
    ↓
PostgreSQL Staging Tables
    ↓
Analytical SQL Views
    ↓
Power BI Data Model
    ↓
Business Dashboard & Data Quality Monitoring
```

---

# Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

Raw CSV files are not stored in this repository due to file size limitations and data management best practices.

To run the project locally, download the dataset and place the required CSV files in:

```text
data/raw/
```

## Required Files

```text
olist_orders_dataset.csv
olist_customers_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

The geolocation dataset is not required for this project.

---

# Key Features

* Automated ETL orchestration with `main.py`
* Dirty data simulation for testing validation logic
* Data transformation and standardization
* Business rule validation
* Rejected records handling
* PostgreSQL staging layer
* ETL validation monitoring table
* Analytical SQL views
* Power BI dashboard integration
* Relational Power BI data model
* Data quality monitoring

---

# Tech Stack

| Area                   | Technologies                       |
| ---------------------- | ---------------------------------- |
| Programming            | Python                             |
| Data Processing        | Pandas                             |
| Database               | PostgreSQL                         |
| ORM / DB Connection    | SQLAlchemy                         |
| Environment Management | python-dotenv                      |
| BI & Reporting         | Power BI                           |
| Database Management    | pgAdmin                            |
| Query Language         | SQL                                |
| Concepts               | ETL, Data Validation, Data Quality |

---

# Project Structure

```text
ecommerce-etl-data-quality-pipeline/
│
├── data/
│   ├── raw/
│   ├── dirty/
│   ├── processed/
│   └── rejected/
│
├── src/
│   ├── make_dirty_data.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   └── 03_create_views.sql
│
├── screenshots/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ETL Process

## 1. Dirty Data Simulation

The pipeline intentionally introduces data quality issues such as:

* Duplicated records
* Missing customer IDs
* Invalid future dates
* Inconsistent order statuses
* Negative payment values

This makes the project closer to real-world data preparation scenarios.

---

## 2. Transformation Layer

The transformation step standardizes and prepares the data before validation.

### Examples

* Date parsing
* Status normalization
* Text formatting
* Numeric conversion
* Duplicate handling
* Preparation of clean intermediate CSV files

---

## 3. Validation Layer

The validation layer applies business rules and separates valid and rejected records.

### Example Validation Rules

* Order ID cannot be null
* Customer ID cannot be null
* Order status must belong to an accepted status list
* Order purchase date cannot be in the future
* Payment value cannot be negative
* Customer state must use a valid two-letter format

Rejected records are saved separately in:

```text
data/rejected/
```

Valid records are saved in:

```text
data/processed/
```

---

## 4. PostgreSQL Loading

Validated data is loaded into PostgreSQL staging tables:

```text
stg_orders
stg_customers
stg_payments
stg_order_items
stg_products
stg_sellers
stg_category_translation
```

The project also creates an ETL monitoring table:

```text
etl_validation_summary
```

### Validation Summary Structure

```text
table_name
valid_rows
rejected_rows
total_rows
success_rate
run_timestamp
```

---

## 5. Analytical SQL Views

The project includes SQL views prepared for analysis and reporting:

```text
vw_sales_summary
vw_payment_distribution
vw_top_customers
vw_data_quality_summary
```

### Analytical Use Cases

* Revenue analysis
* Payment method analysis
* Customer ranking
* Data quality summary

---

# Power BI Integration

The PostgreSQL output is connected to Power BI.

The Power BI report includes:

* Ecommerce KPI overview
* Revenue trend analysis
* Payment method distribution
* Customer and product insights
* ETL validation monitoring
* Rejected rows analysis
* Relational data model based on PostgreSQL staging tables

This creates a complete workflow:

```text
Python ETL → PostgreSQL → SQL Views → Power BI Dashboard
```

---

# Example Metrics

Example results from the ETL validation layer:

```text
orders     | valid: 96,481  | rejected: 2,960 | success rate: 97.02%
customers  | valid: 98,447  | rejected: 1     | success rate: 100.00%
payments   | valid: 102,848 | rejected: 1,038 | success rate: 99.00%
```

---

# Screenshots

## ETL Pipeline Execution

![ETL Pipeline Execution](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-07-164912.png)

---

## PostgreSQL Validation Summary

![PostgreSQL Validation Summary](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-08-105059.png)

---

## Power BI Executive Overview

![Power BI Executive Overview](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-07-234339.png)

---

## Power BI Customer and Product Insights

![Power BI Customer and Product Insights](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-07-234401.png)

---

## Power BI Data Quality Monitoring

![Power BI Data Quality Monitoring](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-07-234350.png)

---

## Power BI Data Model

![Power BI Data Model](http://kuzmasylwester.com/wp-content/uploads/2026/05/Zrzut-ekranu-2026-05-07-211830.png)

---

# How to Run

## 1. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

---

## 2. Create PostgreSQL Database

```sql
CREATE DATABASE ecommerce_etl;
```

---

## 3. Create `.env` File

Use `.env.example` as a template:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_etl
DB_USER=postgres
DB_PASSWORD=your_password_here
```

---

## 4. Place Raw Dataset Files

Place required CSV files in:

```text
data/raw/
```

---

## 5. Run the Full Pipeline

```bash
py src/main.py
```

### Pipeline Steps

```text
1. Generate dirty data
2. Transform data
3. Validate records
4. Load valid data into PostgreSQL
5. Store validation summary
```

---

## 6. Create Analytical SQL Views

Run the SQL script in pgAdmin:

```text
sql/03_create_views.sql
```

---

## 7. Connect Power BI

In Power BI Desktop:

```text
Get Data → PostgreSQL database
```

### Connection Settings

```text
Server: localhost
Database: ecommerce_etl
```

Load:

* Staging tables
* Analytical SQL views
* ETL validation summary table

---

# Data Quality Approach

The project separates transformation and validation logic.

Transformation prepares the data.
Validation decides which records are accepted and which are rejected.

This approach makes the process more transparent and avoids silently deleting problematic records.

---

# What This Project Demonstrates

This project demonstrates practical skills in:

* Building modular ETL pipelines
* Working with relational data
* Cleaning and validating business datasets
* Handling rejected records
* Loading data into PostgreSQL
* Creating analytical SQL views
* Building a Power BI semantic model
* Designing data quality monitoring
* Connecting technical data preparation with business reporting

---

# Repository Notes

Raw datasets and generated files are excluded from GitHub.

## Ignored Folders

```text
data/raw/
data/dirty/
data/processed/
data/rejected/
logs/
reports/
```

## Ignored Environment Files

```text
.env
```

A safe configuration template is provided as:

```text
.env.example
```

---

# Author

**Sylwester Kuźma**

Portfolio: [https://kuzmasylwester.com](https://kuzmasylwester.com)
GitHub: [https://github.com/silverek33](https://github.com/silverek33)

