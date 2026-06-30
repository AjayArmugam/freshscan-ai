from torch.utils.data import DataLoader
from torchvision import transforms

from etl.config import (
    IMAGE_SIZE,
    BATCH_SIZE,
    NUM_WORKERS,
)

from ml.classification.dataset import FreshScanDataset


train_transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
])

val_transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
])


def get_dataloaders():

    train_dataset = FreshScanDataset(
        split="train",
        transform=train_transform,
    )

    val_dataset = FreshScanDataset(
        split="val",
        transform=val_transform,
    )

    test_dataset = FreshScanDataset(
        split="test",
        transform=val_transform,
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=NUM_WORKERS,
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        num_workers=NUM_WORKERS,
    )

    return train_loader, val_loader, test_loader