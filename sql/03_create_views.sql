-- SALES SUMMARY
CREATE OR REPLACE VIEW vw_sales_summary AS
SELECT
    DATE(o.order_purchase_timestamp) AS order_date,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(SUM(p.payment_value)::numeric, 2) AS total_revenue,
    ROUND(AVG(p.payment_value)::numeric, 2) AS avg_order_value
FROM stg_orders o
JOIN stg_payments p ON o.order_id = p.order_id
GROUP BY DATE(o.order_purchase_timestamp)
ORDER BY order_date;


-- TOP CUSTOMERS
CREATE OR REPLACE VIEW vw_top_customers AS
SELECT
    c.customer_unique_id,
    COUNT(o.order_id) AS total_orders,
    ROUND(SUM(p.payment_value)::numeric, 2) AS total_spent
FROM stg_customers c
JOIN stg_orders o ON c.customer_id = o.customer_id
JOIN stg_payments p ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY total_spent DESC
LIMIT 10;


-- PAYMENT TYPE DISTRIBUTION
CREATE OR REPLACE VIEW vw_payment_distribution AS
SELECT
    payment_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(payment_value)::numeric, 2) AS total_value
FROM stg_payments
GROUP BY payment_type
ORDER BY total_value DESC;


-- DATA QUALITY CHECK
CREATE OR REPLACE VIEW vw_data_quality_summary AS
SELECT
    'orders' AS table_name,
    COUNT(*) AS total_rows
FROM stg_orders

UNION ALL

SELECT
    'customers',
    COUNT(*)
FROM stg_customers

UNION ALL

SELECT
    'payments',
    COUNT(*)
FROM stg_payments;