from typing import List
from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


class Kinetics400(DatasetLoader):
    """Kinetics400 Dataset.

    Homepage: https://www.deepmind.com/open-source/kinetics
    Huggingface Dataset: https://huggingface.co/datasets/AlexFierro9/Kinetics400/blob/main/README.md
    """
    path: str = "AlexFierro9/Kinetics400"
    concept_type: List[ConceptType] = [ConceptType.ACTIVITY]

    @classmethod
    def load(cls):
        """Load the dataset."""
        dataset = super().load()
        return dataset[
            "train"
        ]  # This defaults to "train" for .csv, and have nothing to do with the actual split


@add_to_registry
class Kinetics4000Train(Kinetics400):
    split: SplitType = SplitType.TRAIN
    hf_ds_kwargs = {"data_files": "train.csv"}


@add_to_registry
class Kinetics4000Val(Kinetics400):
    split: SplitType = SplitType.VALIDATION
    hf_ds_kwargs = {"data_files": "val.csv"}


@add_to_registry
class Kinetics4000Test(Kinetics400):
    split: SplitType = SplitType.TEST
    hf_ds_kwargs = {"data_files": "test.csv"}
