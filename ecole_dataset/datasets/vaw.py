from .base import DatasetLoader
from ecole_dataset.types import ConceptType
from ecole_dataset.registry import add_to_registry


# Visual Attributes in the Wild (VAW) dataset: https://github.com/adobe-research/vaw_dataset#dataset-setup
# Raw annotations and configs such as attrubte_types can be found at: https://github.com/adobe-research/vaw_dataset/tree/main/data

# Our implemented HF dataset page for VAW: https://huggingface.co/datasets/mikewang/vaw
class VAW(DatasetLoader):
    path = "mikewang/vaw"
    split = "train"
    concept_type = [ConceptType.ATTRIBUTE, ConceptType.OBJECT]