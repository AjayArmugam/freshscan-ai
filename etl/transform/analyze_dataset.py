from pathlib import Path
from collections import Counter
from PIL import Image
import pandas as pd
import json

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw"
METADATA_DIR = BASE_DIR / "data" / "metadata"

METADATA_DIR.mkdir(parents=True, exist_ok=True)

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def analyze_dataset():

    image_files = []

    for ext in VALID_EXTENSIONS:
        image_files.extend(RAW_DATA.rglob(f"*{ext}"))

    logger.info("=" * 60)
    logger.info("FreshScan AI Dataset Analyzer")
    logger.info("=" * 60)

    logger.info(f"Total Images : {len(image_files)}")

    class_counter = Counter()

    widths = []
    heights = []

    for image in image_files:

        class_name = image.parent.name
        class_counter[class_name] += 1

        try:
            with Image.open(image) as img:
                w, h = img.size
                widths.append(w)
                heights.append(h)
        except:
            pass

    logger.info(f"Total Classes : {len(class_counter)}")

    logger.info("\nClass Distribution\n")

    for cls, count in sorted(class_counter.items()):
        logger.info(f"{cls:<25} {count}")

    report = {
        "total_images": len(image_files),
        "total_classes": len(class_counter),
        "min_width": min(widths),
        "max_width": max(widths),
        "min_height": min(heights),
        "max_height": max(heights),
        "average_width": sum(widths) / len(widths),
        "average_height": sum(heights) / len(heights),
    }

    with open(METADATA_DIR / "dataset_report.json", "w") as f:
        json.dump(report, f, indent=4)

    df = pd.DataFrame(
        class_counter.items(),
        columns=["Class", "Images"]
    )

    df.to_csv(
        METADATA_DIR / "class_distribution.csv",
        index=False
    )

    logger.info("\nMetadata generated successfully.")


if __name__ == "__main__":
    analyze_dataset()