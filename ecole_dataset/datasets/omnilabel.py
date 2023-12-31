import os
from PIL import Image
from typing import List
from .base import DatasetLoader
import ecole_dataset
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry

# You should download the dataset and set the environment variables
# https://www.omnilabel.org/dataset/download#h.liddoykhrd2s
def get_prefix_to_dir():
    try:
        return {
            "coco": os.environ["COCO_VAL2017_DIR"],
            "object365": os.environ["OBJECT365_VAL_DIR"],
            "openimagesv5": os.environ["OPEN_IMAGES_V5_TEST_DIR"],
        }
    except KeyError as e:
        raise KeyError(
            f"Error when loading OmniLabel dataset: {e}. "
            "To use OmniLabel dataset, you need to download the dataset following https://www.omnilabel.org/dataset/download#h.liddoykhrd2s, and set the environment variables COCO_VAL2017_DIR, OBJECT365_VAL_DIR, OPEN_IMAGES_V5_TEST_DIR in source.sh to the corresponding directories."
        )

@add_to_registry
class OmniLabel(DatasetLoader):
    """OmniLabel dataset.

    URL: https://www.omnilabel.org
    Huggingface Dataset: https://huggingface.co/datasets/xingyaoww/omnilabel
    """

    path: str = "xingyaoww/omnilabel"
    split: SplitType = SplitType.TEST
    concept_type: List[ConceptType] = [ConceptType.OBJECT]
    hf_ds_kwargs = {
        # Only validation set has annotations available
        # So we use validation set as our test set
        "split": "validation",
    }

    @classmethod
    def load(cls):
        """Load the dataset."""
        dataset = super().load()

        # TODO(xingyao6): load images
        # ecole_dataset.logger.info(
        #     "To use OmniLabel dataset, you need to download the dataset following https://www.omnilabel.org/dataset/download#h.liddoykhrd2s, and set the environment variables COCO_VAL2017_DIR, OBJECT365_VAL_DIR, OPEN_IMAGES_V5_TEST_DIR in source.sh to the corresponding directories."
        # )
        # prefix_to_dir = get_prefix_to_dir()
        # # load image_filename
        # # https://www.omnilabel.org/dataset/download#h.liddoykhrd2s
        # def add_image(example):
        #     # example["image_filename"] = os.path.join("images", example["image_id"] + ".jpg")
        #     prefix, image_filename = example["image_filename"].split("/")
        #     filepath_to_load = os.path.join(prefix_to_dir[prefix], image_filename)

        #     # load into PIL.Image
        #     example["image"] = Image.open(filepath_to_load)
        #     return example

        # dataset = dataset.map(add_image)
        return dataset
