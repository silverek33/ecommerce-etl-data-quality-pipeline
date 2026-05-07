import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

PROCESSED_PATH = "data/processed"

load_dotenv()


def get_engine():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
    )


def load_table(engine, file_name, table_name):
    file_path = os.path.join(PROCESSED_PATH, file_name)
    df = pd.read_csv(file_path)

    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"Loaded {len(df)} rows into {table_name}")


def run():
    engine = get_engine()

    load_table(engine, "orders_valid.csv", "stg_orders")
    load_table(engine, "customers_valid.csv", "stg_customers")
    load_table(engine, "payments_valid.csv", "stg_payments")
    load_table(engine, "order_items_clean.csv", "stg_order_items")
    load_table(engine, "products_clean.csv", "stg_products")
    load_table(engine, "sellers_clean.csv", "stg_sellers")
    load_table(engine, "category_translation_clean.csv", "stg_category_translation")


if __name__ == "__main__":
    run()