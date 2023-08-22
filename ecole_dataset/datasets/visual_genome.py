from .base import DatasetLoader
from ecole_dataset.types import ConceptType
from ecole_dataset.registry import add_to_registry, SplitType

# https://huggingface.co/datasets/visual_genome/blob/main/README.md

class VisualGenome(DatasetLoader):
    path = "visual_genome"
    split = SplitType.TRAIN

@add_to_registry
class VisualGenomeAttributes(VisualGenome):
    concept_type = [ConceptType.ATTRIBUTE]
    name = "attributes_v1.2.0"

@add_to_registry
class VisualGenomeObjects(VisualGenome):
    concept_type = [ConceptType.OBJECT]
    name = "objects_v1.2.0"

@add_to_registry
class VisualGenomeRelationships(VisualGenome):
    concept_type = [ConceptType.RELATIONSHIP]
    name = "relationships_v1.2.0"
