from typing import List
from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


@add_to_registry
class OmniLabel(DatasetLoader):
    """OmniLabel dataset.

    URL: https://www.omnilabel.org
    Huggingface Dataset: https://huggingface.co/datasets/xingyaoww/omnilabel
    """

    path: str = "xingyaoww/omnilabel"
    # Only validation set has annotations available
    split: SplitType = SplitType.VALIDATION
    concept_type: List[ConceptType] = [ConceptType.OBJECT]
