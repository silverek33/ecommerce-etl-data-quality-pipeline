import os
import pandas as pd

PROCESSED_PATH = "data/processed"
REJECTED_PATH = "data/rejected"

os.makedirs(REJECTED_PATH, exist_ok=True)


def save_validation_result(df, invalid, entity_name):
    valid = df.drop(invalid.index)

    invalid.to_csv(
        os.path.join(REJECTED_PATH, f"{entity_name}_rejected.csv"),
        index=False
    )

    valid.to_csv(
        os.path.join(PROCESSED_PATH, f"{entity_name}_valid.csv"),
        index=False
    )

    print(
        f"{entity_name.capitalize()} validated | "
        f"valid: {len(valid)} | rejected: {len(invalid)}"
    )


def validate_orders():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "orders_clean.csv"))

    valid_statuses = [
        "delivered",
        "shipped",
        "canceled",
        "unavailable",
        "invoiced",
        "processing",
        "created",
        "approved",
    ]

    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"], errors="coerce"
    )

    invalid = df[
        df["order_id"].isna()
        | df["customer_id"].isna()
        | ~df["order_status"].isin(valid_statuses)
        | df["order_purchase_timestamp"].isna()
        | (df["order_purchase_timestamp"] > pd.Timestamp.now())
    ]

    save_validation_result(df, invalid, "orders")


def validate_customers():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "customers_clean.csv"))

    invalid = df[
        df["customer_id"].isna()
        | df["customer_unique_id"].isna()
        | df["customer_zip_code_prefix"].isna()
        | df["customer_city"].isna()
        | df["customer_state"].isna()
        | (df["customer_state"].astype(str).str.len() != 2)
    ]

    save_validation_result(df, invalid, "customers")


def validate_payments():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "payments_clean.csv"))

    invalid = df[
        df["order_id"].isna()
        | df["payment_type"].isna()
        | df["payment_value"].isna()
        | (df["payment_value"] < 0)
    ]

    save_validation_result(df, invalid, "payments")


def run():
    validate_orders()
    validate_customers()
    validate_payments()


if __name__ == "__main__":
    run()