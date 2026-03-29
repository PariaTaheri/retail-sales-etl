import pandas as pd
import sqlite3
from transform import clean_data

def run_pipeline():
    raw_file_path = "data/raw/SuperStoreOrders.csv"
    processed_file_path = "data/processed/clean_orders.csv"
    db_path = "data/database.db"

    df = pd.read_csv(raw_file_path)

    clean_df = clean_data(df)

    clean_df.to_csv(processed_file_path, index=False)

    conn = sqlite3.connect(db_path)
    clean_df.to_sql("clean_orders", conn, if_exists="replace", index=False)
    conn.close()

    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()