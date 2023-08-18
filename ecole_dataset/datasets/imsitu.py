from typing import List
from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry


@add_to_registry
class ImSitu(DatasetLoader):
    """ImSitu Dataset.

    Homepage: http://imsitu.org/
    Repository: https://github.com/my89/imSitu
        - The metadata used for imSitu: https://github.com/my89/imSitu#metadata
        - The images can be downloaded following: https://github.com/my89/imSitu#images
        - This HF dataset loads the train.json, val.json and test.json from the repository
    Huggingface Dataset: https://huggingface.co/datasets/mikewang/vaw
    
    IMPORTANT NOTE: The frames field in the loaded HF dataset contains a list of json strings 
        (since the data structure for each verb frame is different). 
        To convert the json strings back to dicts, you can refer to the following example:
        ```
            from datasets import load_dataset
            import json
            dataset = load_dataset("mikewang/imsitu")
            print(dataset['train'][0])
            frames = [json.loads(obj) for obj in dataset['train'][0]['frames']]
            print(frames)
        ```
    """
    path: str = "mikewang/imsitu"
    split: SplitType = SplitType.TRAIN
    concept_type: List[ConceptType] = [ConceptType.ACTIVITY]