from pathlib import Path
from PIL import Image

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw"

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

valid_images = 0
corrupted_images = 0


def validate_dataset():

    global valid_images
    global corrupted_images

    image_files = []

    for ext in VALID_EXTENSIONS:
        image_files.extend(RAW_DATA.rglob(f"*{ext}"))

    logger.info("=" * 60)
    logger.info("FreshScan AI Image Validator")
    logger.info("=" * 60)

    logger.info(f"Found {len(image_files)} images\n")

    for image_path in image_files:

        try:
            with Image.open(image_path) as img:
                img.verify()

            valid_images += 1

        except Exception:

            corrupted_images += 1

            logger.info(f"Corrupted: {image_path}")

    logger.info("\nValidation Complete")
    logger.info("-" * 40)
    logger.info(f"Valid Images     : {valid_images}")
    logger.info(f"Corrupted Images : {corrupted_images}")


if __name__ == "__main__":
    validate_dataset()