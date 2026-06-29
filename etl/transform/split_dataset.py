import shutil
from sklearn.model_selection import train_test_split

from etl.logger import logger
from etl.config import (
    TRAIN_DATASET,
    TEST_DATASET,
    SPLIT_DATA_DIR,
    TRAIN_SIZE,
    RANDOM_STATE,
    VALID_EXTENSIONS,
)


def copy_images(image_paths, destination_root, class_name):
    destination = destination_root / class_name
    destination.mkdir(parents=True, exist_ok=True)

    for image in image_paths:
        shutil.copy2(image, destination / image.name)


def split_dataset():

    logger.info("=" * 60)
    logger.info("FreshScan AI Dataset Splitter")
    logger.info("=" * 60)

    # Remove previous split
    if SPLIT_DATA_DIR.exists():
        shutil.rmtree(SPLIT_DATA_DIR)

    SPLIT_DATA_DIR.mkdir(parents=True, exist_ok=True)

    total_train = 0
    total_val = 0
    total_test = 0

    # -----------------------------
    # Split ORIGINAL TRAIN folder
    # -----------------------------
    class_folders = sorted(
        [
            folder
            for folder in TRAIN_DATASET.iterdir()
            if folder.is_dir()
        ]
    )

    for class_folder in class_folders:

        class_name = class_folder.name

        images = [
            img
            for img in class_folder.iterdir()
            if img.suffix.lower() in VALID_EXTENSIONS
        ]

        if len(images) < 2:
            logger.info(f"Skipping {class_name} (Not enough images)")
            continue

        train_images, val_images = train_test_split(
            images,
            test_size=0.15,
            random_state=RANDOM_STATE,
            shuffle=True,
        )

        copy_images(train_images, SPLIT_DATA_DIR / "train", class_name)
        copy_images(val_images, SPLIT_DATA_DIR / "val", class_name)

        total_train += len(train_images)
        total_val += len(val_images)

        logger.info(
            f"{class_name:<25}"
            f"Train:{len(train_images):>5} "
            f"Val:{len(val_images):>5}"
        )

    # -----------------------------
    # Copy ORIGINAL TEST folder
    # -----------------------------
    logger.info("\nCopying Test Dataset...")

    test_class_folders = sorted(
        [
            folder
            for folder in TEST_DATASET.iterdir()
            if folder.is_dir()
        ]
    )

    for class_folder in test_class_folders:

        class_name = class_folder.name

        images = [
            img
            for img in class_folder.iterdir()
            if img.suffix.lower() in VALID_EXTENSIONS
        ]

        copy_images(images, SPLIT_DATA_DIR / "test", class_name)

        total_test += len(images)

    logger.info("=" * 60)
    logger.info("Dataset Split Complete")
    logger.info("=" * 60)

    logger.info(f"Training Images   : {total_train}")
    logger.info(f"Validation Images : {total_val}")
    logger.info(f"Testing Images    : {total_test}")


if __name__ == "__main__":
    split_dataset()