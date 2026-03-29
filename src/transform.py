import pandas as pd

def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.strip().str.lower()

    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce")
    df["profit"] = pd.to_numeric(df["profit"], errors="coerce")
    df["shipping_cost"] = pd.to_numeric(df["shipping_cost"], errors="coerce")

    df = df.dropna(subset=["order_id", "order_date", "sales"])

    return df

if __name__ == "__main__":
    file_path = "data/raw/SuperStoreOrders.csv"
    df = pd.read_csv(file_path)
    clean_df = clean_data(df)

    print("Cleaned data:")
    print(clean_df.head())
    print(clean_df.info())
    clean_df.to_csv("data/processed/clean_orders.csv", index=False)