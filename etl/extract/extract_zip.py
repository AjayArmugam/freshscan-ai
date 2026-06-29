from pathlib import Path
import zipfile

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw"


def extract_all_zip_files():
    """
    Extract all zip files inside data/raw recursively.
    """

    zip_files = list(RAW_DATA.rglob("*.zip"))

    if not zip_files:
        print("No ZIP files found.")
        return

    print(f"Found {len(zip_files)} ZIP file(s).\n")

    for zip_file in zip_files:

        extract_to = zip_file.parent / zip_file.stem

        print(f"Extracting: {zip_file.name}")

        extract_to.mkdir(exist_ok=True)

        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(extract_to)

        print(f"Extracted to: {extract_to}\n")


if __name__ == "__main__":
    extract_all_zip_files()