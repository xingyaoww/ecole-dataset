from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry

@add_to_registry
class AwA2(DatasetLoader):
    """ 
    Dataset description: An attribute dataset in Animal domain 

    Homepage: https://cvml.ista.ac.at/AwA2/

    HF dataset link: https://huggingface.co/datasets/mikewang/AwA2
    
    IMPORTANT Notes:
        - This HF dataset downloads the dataset (https://cvml.ista.ac.at/AwA2/AwA2-data.zip), and loads the image instances with class-level annotations.
        - The "train" split in this HF dataset contains all the images. For the original proposed splits and the proposed splits version 2.0, please refer to [here](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/zero-shot-learning/zero-shot-learning-the-good-the-bad-and-the-ugly/).
        - License files is also included in the downloaded dataset (https://cvml.ista.ac.at/AwA2/AwA2-data.zip)

    """

    path = "mikewang/AwA2"
    split: SplitType = SplitType.TRAIN
    hf_ds_kwargs = {"split": "train"}
    concept_type = [ConceptType.ATTRIBUTE]