from pathlib import Path
from PIL import Image

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

IMAGE_SIZE = (224, 224)
VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

processed_count = 0


def preprocess_dataset():
    global processed_count

    logger.info("=" * 60)
    logger.info("FreshScan AI Image Preprocessor")
    logger.info("=" * 60)

    image_files = []

    for ext in VALID_EXTENSIONS:
        image_files.extend(RAW_DATA.rglob(f"*{ext}"))

    logger.info(f"Found {len(image_files)} images.\n")

    for image_path in image_files:

        relative_path = image_path.relative_to(RAW_DATA)
        output_path = PROCESSED_DATA / relative_path

        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with Image.open(image_path) as img:

                img = img.convert("RGB")
                img = img.resize(IMAGE_SIZE)

                output_path = output_path.with_suffix(".jpg")

                img.save(output_path, quality=95)

                processed_count += 1

        except Exception as e:
            logger.error(f"Failed: {image_path}")
            logger.error(e)

    logger.info("\n------------------------------------------")
    logger.info(f"Images Processed : {processed_count}")
    logger.info(f"Saved to         : {PROCESSED_DATA}")
    logger.info("------------------------------------------")


if __name__ == "__main__":
    preprocess_dataset()