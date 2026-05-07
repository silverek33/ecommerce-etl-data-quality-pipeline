import os
import pandas as pd

DIRTY_PATH = "data/dirty"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)


def clean_orders():
    df = pd.read_csv(os.path.join(DIRTY_PATH, "orders_dirty.csv"))

    df["order_status"] = df["order_status"].astype(str).str.lower().str.strip()

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df = df.drop_duplicates(subset=["order_id"])

    df.to_csv(os.path.join(PROCESSED_PATH, "orders_clean.csv"), index=False)
    print("Orders transformed")


def clean_customers():
    df = pd.read_csv(os.path.join(DIRTY_PATH, "customers_dirty.csv"))

    df["customer_city"] = df["customer_city"].astype(str).str.lower().str.strip()
    df["customer_state"] = df["customer_state"].astype(str).str.upper().str.strip()

    df = df.drop_duplicates(subset=["customer_id"], keep="first")

    df.to_csv(os.path.join(PROCESSED_PATH, "customers_clean.csv"), index=False)
    print("Customers transformed")


def clean_payments():
    df = pd.read_csv(os.path.join(DIRTY_PATH, "payments_dirty.csv"))

    df["payment_type"] = df["payment_type"].astype(str).str.lower().str.strip()
    df["payment_value"] = pd.to_numeric(df["payment_value"], errors="coerce")

    df.to_csv(os.path.join(PROCESSED_PATH, "payments_clean.csv"), index=False)
    print("Payments transformed")


def copy_other_tables():
    tables = [
        "order_items_dirty.csv",
        "products_dirty.csv",
        "sellers_dirty.csv",
        "category_translation_dirty.csv",
    ]

    for table in tables:
        df = pd.read_csv(os.path.join(DIRTY_PATH, table))
        clean_name = table.replace("_dirty", "_clean")
        df.to_csv(os.path.join(PROCESSED_PATH, clean_name), index=False)

    print("Other tables copied")


def run():
    clean_orders()
    clean_customers()
    clean_payments()
    copy_other_tables()


if __name__ == "__main__":
    run()