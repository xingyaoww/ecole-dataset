from typing import Union, List, Tuple, Any, Optional
from datasets import (
    load_dataset,
    Dataset,
    DatasetDict,
    IterableDatasetDict,
    IterableDataset,
)

from ecole_dataset.types import ConceptType, SplitType


class DatasetLoader:
    """Load datasets from the HuggingFace Hub or from local files."""

    # path and name to the dataset in the HuggingFace Hub
    # or optionally a different path if you override the .load method
    # for custom loading
    path: str
    name: str
    split: SplitType
    concept_type: List[ConceptType]

    @classmethod
    def load(cls) -> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
        """Load the dataset."""
        dataset = load_dataset(
            cls.path,
            cls.name,
            split=cls.split.value,
        )
        return dataset


class DatasetMixtureLoader:
    """Load a mixture of DatasetLoader."""

    def __init__(self, datasets: list[DatasetLoader]):
        """Initialize the dataset mixture loader."""
        self.datasets = datasets

    def load(
        self,
    ) -> List[
        Tuple[str, Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]]
    ]:
        """Load the dataset."""
        return [
            (dataset.__class__.__name__, dataset.load())
            for dataset in self.datasets
        ]
