from ml.classification.dataloader import get_dataloaders


def main():

    train_loader, val_loader, test_loader = get_dataloaders()

    print("=" * 50)
    print("FreshScan DataLoader Test")
    print("=" * 50)

    print(f"Train Batches : {len(train_loader)}")
    print(f"Val Batches   : {len(val_loader)}")
    print(f"Test Batches  : {len(test_loader)}")

    images, labels = next(iter(train_loader))

    print(f"Batch Shape   : {images.shape}")
    print(f"Labels Shape  : {labels.shape}")


if __name__ == "__main__":
    main()