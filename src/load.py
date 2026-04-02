import logging
import pandas as pd
import os


def load(df, output_path="data/processed/clean_data.csv"):
    """
    Load transformed data to CSV
    """
    logging.info("Load step started")

    try:
        # 🔹 create folder if not exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 🔹 save file
        df.to_csv(output_path, index=False)

        logging.info(f"Data saved to {output_path}")

    except Exception as e:
        logging.error(f"Error in load step: {e}")
        raise