from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent

DATASETS = [
    {
        "name": "Fresh and Rotten Fruits",
        "source": "Kaggle",
        "slug": "swoyam2609/fresh-and-stale-classification",
        "output": BASE_DIR / "data/raw/classification/fruits",
    },
]

print("=" * 60)
print("FreshScan AI Dataset Downloader")
print("=" * 60)

for dataset in DATASETS:
    print(f"\nDownloading: {dataset['name']}")

    dataset["output"].mkdir(parents=True, exist_ok=True)

    command = [
        "kaggle",
        "datasets",
        "download",
        "-d",
        dataset["slug"],
        "-p",
        str(dataset["output"]),
    ]

    subprocess.run(command)

print("\nDownload process completed.")