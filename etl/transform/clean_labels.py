from pathlib import Path
import shutil

from etl.logger import logger

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw"

# Mapping of incorrect folder names to correct folder names
CLASS_MAPPING = {
    "freshpatato": "freshpotato",
    "rottenpatato": "rottenpotato",
    "freshtamto": "freshtomato",
    "rottentamto": "rottentomato",
}


def merge_folders(source: Path, destination: Path):
    """
    Move all files from source folder into destination folder.
    """

    destination.mkdir(parents=True, exist_ok=True)

    for file in source.iterdir():
        shutil.move(str(file), str(destination / file.name))

    source.rmdir()


def clean_labels():

    logger.info("=" * 60)
    logger.info("FreshScan AI Label Cleaner")
    logger.info("=" * 60)

    renamed = 0

    for folder in RAW_DATA.rglob("*"):

        if not folder.is_dir():
            continue

        folder_name = folder.name.lower()

        if folder_name in CLASS_MAPPING:

            new_name = CLASS_MAPPING[folder_name]
            destination = folder.parent / new_name

            logger.info(f"\nFixing: {folder.name} -> {new_name}")

            merge_folders(folder, destination)

            renamed += 1

    logger.info("\n--------------------------------------")
    logger.info(f"Folders Fixed : {renamed}")
    logger.info("--------------------------------------")


if __name__ == "__main__":
    clean_labels()