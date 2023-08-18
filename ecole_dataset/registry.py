from typing import Optional, List
from collections import namedtuple
from datasets import load_dataset as hf_load_dataset

from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.datasets.base import DatasetLoader, DatasetMixtureLoader

REGISTERED_DATASET: List[DatasetLoader] = []

def add_to_registry(dataloader: DatasetLoader):
    REGISTERED_DATASET.append(dataloader)
    return dataloader


def load_datasets(concept_type: ConceptType, split: SplitType):
    ret = []
    for dataset in REGISTERED_DATASET:
        if concept_type in dataset.concept_type and split == dataset.split:
            ret.append(dataset)
    return DatasetMixtureLoader(ret)
