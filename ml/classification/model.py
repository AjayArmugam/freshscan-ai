import torch.nn as nn
from torchvision import models

from etl.config import NUM_CLASSES, PRETRAINED


class FreshScanClassifier(nn.Module):

    def __init__(self):

        super().__init__()

        if PRETRAINED:
            weights = models.EfficientNet_B0_Weights.DEFAULT
        else:
            weights = None

        self.model = models.efficientnet_b0(weights=weights)

        in_features = self.model.classifier[1].in_features

        self.model.classifier[1] = nn.Linear(
            in_features,
            NUM_CLASSES
        )

    def forward(self, x):

        return self.model(x)