import os
import pandas as pd

RAW_PATH = "data/raw"
DIRTY_PATH = "data/dirty"

os.makedirs(DIRTY_PATH, exist_ok=True)


def save_dirty_copy(input_file, output_file):
    df = pd.read_csv(os.path.join(RAW_PATH, input_file))
    df.to_csv(os.path.join(DIRTY_PATH, output_file), index=False)
    print(f"Copied {input_file} -> {output_file}")


def make_orders_dirty():
    df = pd.read_csv(os.path.join(RAW_PATH, "olist_orders_dataset.csv"))

    df = pd.concat([df, df.sample(100, random_state=42)], ignore_index=True)
    df.loc[df.sample(frac=0.01, random_state=1).index, "order_purchase_timestamp"] = "2099-01-01"
    df.loc[df.sample(frac=0.02, random_state=2).index, "order_status"] = "Completed"

    df.to_csv(os.path.join(DIRTY_PATH, "orders_dirty.csv"), index=False)
    print("Created orders_dirty.csv")


def make_customers_dirty():
    df = pd.read_csv(os.path.join(RAW_PATH, "olist_customers_dataset.csv"))

    df = pd.concat([df, df.sample(50, random_state=42)], ignore_index=True)
    df.loc[df.sample(frac=0.01, random_state=3).index, "customer_id"] = None

    df.to_csv(os.path.join(DIRTY_PATH, "customers_dirty.csv"), index=False)
    print("Created customers_dirty.csv")


def make_payments_dirty():
    df = pd.read_csv(os.path.join(RAW_PATH, "olist_order_payments_dataset.csv"))

    df.loc[df.sample(frac=0.01, random_state=4).index, "payment_value"] *= -1

    df.to_csv(os.path.join(DIRTY_PATH, "payments_dirty.csv"), index=False)
    print("Created payments_dirty.csv")


def run():
    make_orders_dirty()
    make_customers_dirty()
    make_payments_dirty()

    save_dirty_copy("olist_order_items_dataset.csv", "order_items_dirty.csv")
    save_dirty_copy("olist_products_dataset.csv", "products_dirty.csv")
    save_dirty_copy("olist_sellers_dataset.csv", "sellers_dirty.csv")
    save_dirty_copy("product_category_name_translation.csv", "category_translation_dirty.csv")


if __name__ == "__main__":
    run()