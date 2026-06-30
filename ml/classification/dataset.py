from pathlib import Path

from torch.utils.data import Dataset

from etl.config import SPLIT_DATA_DIR, VALID_EXTENSIONS

from PIL import Image

class FreshScanDataset(Dataset):

    def __init__(self, split="train", transform=None):

        self.transform = transform
        self.data_dir = SPLIT_DATA_DIR / split

        self.classes = sorted(
            [
                folder.name
                for folder in self.data_dir.iterdir()
                if folder.is_dir()
            ]
        )

        self.class_to_idx = {
            class_name: idx
            for idx, class_name in enumerate(self.classes)
        }

        self.idx_to_class = {
            idx: class_name
            for class_name, idx in self.class_to_idx.items()
        }

        self.samples = []

        for class_name in self.classes:

            class_folder = self.data_dir / class_name

            for image_path in class_folder.iterdir():

                if image_path.suffix.lower() in VALID_EXTENSIONS:

                    self.samples.append(
                        (image_path, self.class_to_idx[class_name])
                    )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):

            image_path, label = self.samples[index]

            image = Image.open(image_path).convert("RGB")

            if self.transform:
                image = self.transform(image)

            return image, label