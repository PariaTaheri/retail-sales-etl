import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("Data loaded successfully")
    print(df.head())
    return df

if __name__ == "__main__":
    file_path = "data/raw/SuperStoreOrders.csv"
    df = extract_data(file_path)