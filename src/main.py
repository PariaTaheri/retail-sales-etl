import logging
from extract import extract
from transform import transform
from load import load


logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    logging.info("Pipeline started")

    file_path = "data/raw/SuperStoreOrders.csv"

    df = extract(file_path)
    df = transform(df)
    load(df)

    logging.info("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()