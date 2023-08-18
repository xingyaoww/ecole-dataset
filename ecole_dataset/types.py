from enum import Enum
from collections import namedtuple

class ConceptType(Enum):
    OBJECT = "object"
    ATTRIBUTE = "attribute"
    AFFORDANCE = "affordance"
    RELATIONSHIP = "relationship"
    ACTIVITY = "activity"

class SplitType(Enum):
    TRAIN = "train"
    VALID = "valid"
    TEST = "test"
