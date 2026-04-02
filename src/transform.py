import logging
import pandas as pd


def transform(df):
    """
    Clean and transform raw data
    """
    logging.info("Transform step started")

    try:
        df = df.copy()

        # 🔹 1. Standardize column names (lowercase + underscore)
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # 🔹 2. Remove duplicates
        df = df.drop_duplicates()

        # 🔹 3. Handle missing values (example)
        df = df.dropna(subset=["order_date", "ship_date"])

        # 🔹 4. Convert date columns
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

        # 🔹 5. Create new feature (very important in real jobs)
        df["processing_days"] = (df["ship_date"] - df["order_date"]).dt.days

        # 🔹 6. Remove negative values (data quality check)
        df = df[df["processing_days"] >= 0]

        logging.info("Transform step finished successfully")

        return df

    except Exception as e:
        logging.error(f"Error in transform step: {e}")
        raise