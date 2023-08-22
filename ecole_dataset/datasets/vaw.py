from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


class VAW(DatasetLoader):
    """Visual Attributes in the Wild (VAW) dataset.

    https://github.com/adobe-research/vaw_dataset#dataset-setup

    Raw annotations and configs such as attrubte_types can be found at: https://github.com/adobe-research/vaw_dataset/tree/main/data

    Our implemented HF dataset page for VAW: https://huggingface.co/datasets/mikewang/vaw
    """

    path = "mikewang/vaw"
    concept_type = [ConceptType.ATTRIBUTE, ConceptType.OBJECT]


@add_to_registry
class VAWTrain(VAW):
    split = SplitType.TRAIN
    hf_ds_kwargs = {"split": "train"}


@add_to_registry
class VAWVal(VAW):
    split = SplitType.VALIDATION
    hf_ds_kwargs = {"split": "validation"}


@add_to_registry
class VAWTest(VAW):
    split = SplitType.TEST
    hf_ds_kwargs = {"split": "test"}
