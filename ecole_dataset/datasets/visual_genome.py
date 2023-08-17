from .base import DatasetLoader

class VisualGenome(DatasetLoader):
    path = "visual_genome"
    split = "train"

class VisualGenomeAttributes(VisualGenome):
    name = "attributes_v1.2.0"

class VisualGenomeObjects(VisualGenome):
    name = "objects_v1.2.0"

class VisualGenomeQA(VisualGenome):
    name = "question_answers_v1.2.0"

class VisualGenomeRegionDescriptions(VisualGenome):
    name = "region_descriptions_v1.2.0"

class VisualGenomeRelationships(VisualGenome):
    name = "relationships_v1.2.0"
