from typing import Optional, List, Mapping
from datasets import Dataset
import ecole_dataset
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.datasets.base import DatasetLoader

REGISTERED_DATASET: List[DatasetLoader] = []


def add_to_registry(dataloader: DatasetLoader):
    REGISTERED_DATASET.append(dataloader)
    return dataloader


def load_datasets(
    concept_type: Optional[ConceptType] = None,
    split: Optional[SplitType] = None
) -> Mapping[str, Dataset]:
    """Load all datasets that match the concept_type and split."""
    ret = {}
    for dataset in REGISTERED_DATASET:
        if (concept_type is None or concept_type in dataset.concept_type) and (
            split is None or dataset.split == split
        ):
            ret[dataset.__name__] = dataset.load()

    ecole_dataset.logger.info(
        f"Loaded {len(ret)} datasets: {', '.join(ret.keys())}"
    )
    return ret

def load_dataset(
    name: str,
) -> Dataset:
    """Load a dataset by name."""
    for dataset in REGISTERED_DATASET:
        if dataset.__name__ == name:
            return dataset.load()
    raise ValueError(f"Dataset {name} not found")