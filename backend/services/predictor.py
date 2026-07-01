import json

import torch
from PIL import Image
from torchvision import transforms

from etl.config import (
    DEVICE,
    IMAGE_SIZE,
    MODEL_SAVE_PATH,
    CLASS_MAPPING_PATH,
)

from ml.classification.model import FreshScanClassifier


class Predictor:

    def __init__(self):

        self.device = DEVICE

        self.model = FreshScanClassifier().to(self.device)

        self.model.load_state_dict(
            torch.load(
                MODEL_SAVE_PATH,
                map_location=self.device,
            )
        )

        self.model.eval()

        with open(CLASS_MAPPING_PATH, "r") as f:
            self.class_mapping = json.load(f)

        self.transform = transforms.Compose([
            transforms.Resize(IMAGE_SIZE),
            transforms.ToTensor(),
        ])

    def predict(self, image: Image.Image):

        image = image.convert("RGB")

        image = self.transform(image)

        image = image.unsqueeze(0).to(self.device)

        with torch.no_grad():

            outputs = self.model(image)

            probabilities = torch.softmax(outputs, dim=1)

            confidence, predicted = torch.max(probabilities, dim=1)

        class_name = self.class_mapping[str(predicted.item())]

        return {
            "prediction": class_name,
            "confidence": round(confidence.item() * 100, 2),
        }


predictor = Predictor()