import torch
import torch.nn as nn

from etl.config import (
    DEVICE,
    MODEL_SAVE_PATH,
)

from ml.classification.dataloader import get_dataloaders
from ml.classification.model import FreshScanClassifier
from ml.classification.trainer import validate_one_epoch


def evaluate():

    _, _, test_loader = get_dataloaders()

    model = FreshScanClassifier().to(DEVICE)

    model.load_state_dict(
        torch.load(
            MODEL_SAVE_PATH,
            map_location=DEVICE,
        )
    )

    criterion = nn.CrossEntropyLoss()

    test_loss, test_accuracy = validate_one_epoch(
        model=model,
        dataloader=test_loader,
        criterion=criterion,
        device=DEVICE,
    )

    print("=" * 60)
    print("FreshScan AI Evaluation")
    print("=" * 60)

    print(f"Test Loss     : {test_loss:.4f}")
    print(f"Test Accuracy : {test_accuracy * 100:.2f}%")


if __name__ == "__main__":
    evaluate()