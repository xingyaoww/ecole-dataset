from datasets import Split
from enum import Enum
from collections import namedtuple

class ConceptType(Enum):
    OBJECT = "object"
    ATTRIBUTE = "attribute"
    AFFORDANCE = "affordance"
    RELATIONSHIP = "relationship"
    ACTIVITY = "activity"

SplitType = Split
