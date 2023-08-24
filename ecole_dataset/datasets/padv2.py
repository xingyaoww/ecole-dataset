from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry

@add_to_registry
class PADv2(DatasetLoader):
    """ 
    Official Repo: https://github.com/lhc1224/OSAD_Net#-dataset-;

    HF dataset link: https://huggingface.co/datasets/mikewang/padv2
    
    IMPORTANT Notes:

    - This Huggingface dataset loads the Part1 of the Padv2 dataset, i.e., the PADv2_part1.zip; The file can also be downloaded from: https://uofi.box.com/s/1atjh3d2p82qyxm3gp11514006va0llq
    - Each instance in the loaded HF dataset contains the following fields:
        - image_uid: unique id to a dataset instanec
        - image_path: path to the raw rgb image
        - depth_path: path to the depth annotation of the image
        - mask_path: path to the object mask of the image
        - affordance_type: affordance type of the object in the image
        - original_divisions: there are three versions of divisions on the affordance types in the original dataset, this field stores the split ("train" or "test") of this instance in the three different divisions ("divide_1", "divide_2", "divide_3")
    """

    path = "mikewang/padv2"
    concept_type = [ConceptType.AFFORDANCE]