import time

from make_dirty_data import run as make_dirty
from transform import run as transform_data
from validate import run as validate_data
from load import run as load_data


def run_pipeline():
    start_time = time.time()

    print("=" * 50)
    print("STARTING ETL PIPELINE")
    print("=" * 50)

    print("\n[1/4] Generating dirty data...")
    make_dirty()

    print("\n[2/4] Transforming data...")
    transform_data()

    print("\n[3/4] Validating data...")
    validate_data()

    print("\n[4/4] Loading data to PostgreSQL...")
    load_data()

    end_time = time.time()

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETED")
    print(f"Execution time: {round(end_time - start_time, 2)} seconds")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()