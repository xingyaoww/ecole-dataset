import json
from typing import List, Union
from datasets import (
    Dataset,
    DatasetDict,
    IterableDatasetDict,
    IterableDataset,
    DatasetInfo,
)
from cached_path import cached_path

from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


@add_to_registry
class OmniLabel(DatasetLoader):
    path: str = "https://huggingface.co/datasets/xingyaoww/omnilabel/resolve/main/dataset_all_val_v0.1.3.json"
    name: str = "omnilabel"
    split: SplitType = SplitType.VALID  # Only validation set has annotations available
    concept_type: List[ConceptType] = [ConceptType.OBJECT]

    @classmethod
    def load(cls) -> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
        """Load the dataset."""
        with open(cached_path(cls.path)) as f:
            data = json.load(f)

        IMAGE_ID_TO_TO_FILENAME = {}
        for image_info in data["images"]:
            IMAGE_ID_TO_TO_FILENAME[image_info["id"]] = image_info["file_name"]

        DESCRIPTION_ID_TO_DESC = {}
        for desc in data["descriptions"]:
            DESCRIPTION_ID_TO_DESC[desc["id"]] = desc

        def yield_annotation():
            for anno in data["annotations"]:
                image_id = anno["image_id"]
                image_filename = IMAGE_ID_TO_TO_FILENAME[image_id]
                description_ids = anno["description_ids"]
                descriptions = [
                    DESCRIPTION_ID_TO_DESC[description_id]["text"]
                    for description_id in description_ids
                ]

                yield {
                    "id": anno["id"],
                    "image_id": image_id,
                    # TODO: make this a PIL.Image
                    "image_filename": image_filename,
                    "bbox": anno["bbox"],
                    "descriptions": descriptions,
                }

        info = DatasetInfo(
            description="OmniLabel dataset." + json.dumps(data["info"]),
            homepage="https://www.omnilabel.org",
        )
        dataset = Dataset.from_generator(
            yield_annotation,
            info=info,
        )
        return dataset
