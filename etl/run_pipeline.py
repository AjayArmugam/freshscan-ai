from etl.logger import logger

from etl.extract.extract_zip import extract_all_zip_files
from etl.transform.validate_images import validate_dataset
from etl.transform.clean_labels import clean_labels
from etl.transform.analyze_dataset import analyze_dataset
from etl.transform.preprocess_images import preprocess_dataset
from etl.transform.split_dataset import split_dataset


def run_pipeline():
    logger.info("=" * 60)
    logger.info("FreshScan AI ETL Pipeline Started")
    logger.info("=" * 60)

    # Step 1
    logger.info("Step 1/6 : Extracting ZIP files...")
    extract_all_zip_files()

    # Step 2
    logger.info("Step 2/6 : Validating images...")
    validate_dataset()

    # Step 3
    logger.info("Step 3/6 : Cleaning labels...")
    clean_labels()

    # Step 4
    logger.info("Step 4/6 : Analyzing dataset...")
    analyze_dataset()

    # Step 5
    logger.info("Step 5/6 : Preprocessing images...")
    preprocess_dataset()

    # Step 6
    logger.info("Step 6/6 : Splitting dataset...")
    split_dataset()

    logger.info("=" * 60)
    logger.info("FreshScan AI ETL Pipeline Completed Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    run_pipeline()