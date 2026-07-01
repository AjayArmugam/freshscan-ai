import json

from etl.config import CLASS_MAPPING_PATH


def save_class_mapping(dataset):

    mapping = {
        str(idx): class_name
        for idx, class_name in dataset.idx_to_class.items()
    }

    with open(CLASS_MAPPING_PATH, "w") as f:
        json.dump(mapping, f, indent=4)


def load_class_mapping():

    with open(CLASS_MAPPING_PATH, "r") as f:
        return json.load(f)