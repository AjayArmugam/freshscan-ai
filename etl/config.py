from pathlib import Path
import torch

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
ARTIFACTS_DIR = BASE_DIR / "artifacts"

# ==========================================================
# Data Directories
# ==========================================================

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SPLIT_DATA_DIR = DATA_DIR / "split"
METADATA_DIR = DATA_DIR / "metadata"

# ==========================================================
# Dataset Paths
# ==========================================================

CLASSIFICATION_DATASET = (
    PROCESSED_DATA_DIR
    / "classification"
    / "fruits"
    / "fresh-and-stale-classification"
)

TRAIN_DATASET = CLASSIFICATION_DATASET / "Train"
TEST_DATASET = CLASSIFICATION_DATASET / "Test"

# ==========================================================
# Artifacts
# ==========================================================

MODELS_DIR = ARTIFACTS_DIR / "models"
REPORTS_DIR = ARTIFACTS_DIR / "reports"
LOGS_DIR = ARTIFACTS_DIR / "logs"

# ==========================================================
# Image Configuration
# ==========================================================

IMAGE_SIZE = (224, 224)

VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}

# ==========================================================
# Dataset Split Configuration
# ==========================================================

TRAIN_SIZE = 0.85
VAL_SIZE = 0.15

# The original dataset already contains a Test folder.
# We split only Train -> Train + Validation.

# ==========================================================
# Random Seed
# ==========================================================

RANDOM_STATE = 42

# ==========================================================
# Model Configuration
# ==========================================================

MODEL_NAME = "efficientnet_b0"
PRETRAINED = True
NUM_CLASSES = 18

# ==========================================================
# Training Configuration
# ==========================================================

BATCH_SIZE = 32
NUM_WORKERS = 0

EPOCHS = 1

LEARNING_RATE = 1e-4
WEIGHT_DECAY = 1e-4

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_SAVE_PATH = MODELS_DIR / "freshscan_classifier.pth"

METADATA_SAVE_DIR = ARTIFACTS_DIR / "metadata"

CLASS_MAPPING_PATH = METADATA_SAVE_DIR / "class_mapping.json"

METADATA_SAVE_DIR.mkdir(parents=True, exist_ok=True)
# ==========================================================
# Create Required Directories
# ==========================================================

for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    SPLIT_DATA_DIR,
    METADATA_DIR,
    ARTIFACTS_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    LOGS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)