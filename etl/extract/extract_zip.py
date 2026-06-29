from pathlib import Path
import zipfile

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw"


def extract_all_zip_files():
    """
    Extract all ZIP files inside data/raw recursively.
    Skip extraction if the dataset is already extracted.
    """

    zip_files = list(RAW_DATA.rglob("*.zip"))

    if not zip_files:
        logger.info("No ZIP files found.")
        return

    logger.info(f"Found {len(zip_files)} ZIP file(s).")

    for zip_file in zip_files:

        extract_to = zip_file.parent / zip_file.stem

        # Skip extraction if already extracted
        if extract_to.exists() and any(extract_to.iterdir()):
            logger.info(f"Dataset already extracted. Skipping: {zip_file.name}")
            continue

        logger.info(f"Extracting: {zip_file.name}")

        extract_to.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(extract_to)

        logger.info(f"Extracted to: {extract_to}")


if __name__ == "__main__":
    extract_all_zip_files()