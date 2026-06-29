from pathlib import Path
from PIL import Image

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

    print("=" * 60)
    print("FreshScan AI Image Validator")
    print("=" * 60)

    print(f"Found {len(image_files)} images\n")

    for image_path in image_files:

        try:
            with Image.open(image_path) as img:
                img.verify()

            valid_images += 1

        except Exception:

            corrupted_images += 1

            print(f"Corrupted: {image_path}")

    print("\nValidation Complete")
    print("-" * 40)
    print(f"Valid Images     : {valid_images}")
    print(f"Corrupted Images : {corrupted_images}")


if __name__ == "__main__":
    validate_dataset()