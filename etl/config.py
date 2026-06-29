from pathlib import Path

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
# Dataset Split
# ==========================================================

TRAIN_SIZE = 0.85
VAL_SIZE = 0.15

# NOTE:
# The dataset already provides a Test folder.
# Therefore we split only Train -> Train + Validation.
# TEST_SIZE is not required anymore.

# ==========================================================
# Random Seed
# ==========================================================

RANDOM_STATE = 42

# ==========================================================
# Training Configuration (Sprint 2)
# ==========================================================

BATCH_SIZE = 32
NUM_WORKERS = 4

LEARNING_RATE = 1e-4
WEIGHT_DECAY = 1e-4

NUM_EPOCHS = 30

MODEL_NAME = "efficientnet_b0"

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