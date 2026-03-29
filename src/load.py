import pandas as pd
import sqlite3

def load_data(file_path):
    df = pd.read_csv(file_path)

    conn = sqlite3.connect("data/database.db")

    df.to_sql("clean_orders", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print("Data loaded into database")


def read_data():
    conn = sqlite3.connect("data/database.db")
    df = pd.read_sql("SELECT * FROM clean_orders LIMIT 5", conn)
    print(df)
    conn.close()


if __name__ == "__main__":
    file_path = "data/processed/clean_orders.csv"
    load_data(file_path)
    read_data()