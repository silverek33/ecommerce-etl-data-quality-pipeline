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

    result = {
        "table_name": entity_name,
        "valid_rows": len(valid),
        "rejected_rows": len(invalid),
        "total_rows": len(df)
    }

    success_rate = round((len(valid) / len(df)) * 100, 2)

    print(
        f"{entity_name.capitalize()} validated | "
        f"valid: {len(valid)} | rejected: {len(invalid)} | "
        f"success rate: {success_rate}%"
    )

    return result


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

    return save_validation_result(df, invalid, "orders")


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

    return save_validation_result(df, invalid, "customers")


def validate_payments():
    df = pd.read_csv(os.path.join(PROCESSED_PATH, "payments_clean.csv"))

    invalid = df[
        df["order_id"].isna()
        | df["payment_type"].isna()
        | df["payment_value"].isna()
        | (df["payment_value"] < 0)
    ]

    return save_validation_result(df, invalid, "payments")


def run():
    results = []

    results.append(validate_orders())
    results.append(validate_customers())
    results.append(validate_payments())

    return results


if __name__ == "__main__":
    run()