from typing import List
from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


@add_to_registry
class Kinetics400(DatasetLoader):
    """Kinetics400 Dataset.

    Homepage: https://www.deepmind.com/open-source/kinetics
    Huggingface Dataset: https://huggingface.co/datasets/AlexFierro9/Kinetics400/blob/main/README.md
    """
    path: str = "AlexFierro9/Kinetics400"
    split: SplitType = None  # We specify the split in the data_files
    concept_type: List[ConceptType] = [ConceptType.ACTIVITY]
    kwargs = {
        "data_files": "test.csv"
    }
