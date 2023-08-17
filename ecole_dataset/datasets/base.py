from typing import Union, List, Tuple, Any, Optional
from datasets import (
    load_dataset,
    Dataset,
    DatasetDict,
    IterableDatasetDict,
    IterableDataset,
)

from ecole_dataset.types import PreprocessorType, ConceptType


class DatasetLoader:
    """Load datasets from the HuggingFace Hub."""

    # path and name to the dataset in the HuggingFace Hub
    path: str
    name: str
    split: str
    concept_type: List[ConceptType]
    preprocessors: List[PreprocessorType] = []

    @property
    def dataset_id(self) -> str:
        """Return the dataset ID."""
        return f"{self.path}/{self.name}:{self.split}"

    @classmethod
    def load(cls) -> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
        """Load the dataset."""
        dataset = load_dataset(
            cls.path,
            cls.name,
            split=cls.split,
        )

        if cls.preprocessors:
            for preprocessor in cls.preprocessors:
                dataset = dataset.map(preprocessor.function, preprocessor.kwargs)

        return dataset


class DatasetMixtureLoader:
    """Load a mixture of datasets from the HuggingFace Hub."""

    def __init__(self, datasets: list[DatasetLoader]):
        """Initialize the dataset mixture loader."""
        self.datasets = datasets

    def load(
        self,
    ) -> List[
        Tuple[str, Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]]
    ]:
        """Load the dataset."""
        return [(dataset.dataset_id, dataset.load()) for dataset in self.datasets]
