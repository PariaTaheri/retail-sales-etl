import pandas as pd
import logging


def extract(file_path):
    """
    Extract data from CSV file
    """
    logging.info("Extract step started")

    try:
        df = pd.read_csv(file_path)
        logging.info("Data loaded successfully")
        return df

    except Exception as e:
        logging.error(f"Error in extract step: {e}")
        raise