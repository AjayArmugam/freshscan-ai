import torch
import torch.nn as nn
import torch.optim as optim

from etl.config import (
    DEVICE,
    EPOCHS,
    LEARNING_RATE,
    WEIGHT_DECAY,
    MODEL_SAVE_PATH,
)

from ml.classification.dataloader import get_dataloaders
from ml.classification.model import FreshScanClassifier
from ml.classification.trainer import (
    train_one_epoch,
    validate_one_epoch,
)
from ml.classification.utils import save_checkpoint
from ml.classification.class_mapping import save_class_mapping

def train():

    train_loader, val_loader, test_loader = get_dataloaders()

    model = FreshScanClassifier().to(DEVICE)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
    )

    print("=" * 60)
    print("FreshScan AI Training")
    print("=" * 60)
    print(f"Device : {DEVICE}")
    print()

    best_val_loss = float("inf")

    for epoch in range(EPOCHS):

        train_loss, train_acc = train_one_epoch(
            model=model,
            dataloader=train_loader,
            criterion=criterion,
            optimizer=optimizer,
            device=DEVICE,
        )

        val_loss, val_acc = validate_one_epoch(
            model=model,
            dataloader=val_loader,
            criterion=criterion,
            device=DEVICE,
        )

        print(
            f"Epoch [{epoch+1}/{EPOCHS}] | "
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_acc*100:.2f}% | "
            f"Val Loss: {val_loss:.4f} | "
            f"Val Acc: {val_acc*100:.2f}%"
        )

        if val_loss < best_val_loss:

            best_val_loss = val_loss

            save_checkpoint(
                model,
                MODEL_SAVE_PATH,
            )
    
    save_class_mapping(train_loader.dataset)

    print("\nTraining Finished Successfully.")


if __name__ == "__main__":
    train()