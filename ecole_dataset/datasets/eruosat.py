from .base import DatasetLoader
from ecole_dataset.types import ConceptType, SplitType
from ecole_dataset.registry import add_to_registry

@add_to_registry
class EuroSAT(DatasetLoader):
    """ 
    **Homepage:** https://github.com/phelber/EuroSAT

    **IMPORTANT NOTES**
    - This HF dataset downloads the RGB images of the EuroSAT dataset: https://zenodo.org/record/7711810#.ZAm3k-zMKEA; i.e., the EuroSAT_RGB.zip
    """

    path = "mikewang/EuroSAT"
    split: SplitType = SplitType.TRAIN
    hf_ds_kwargs = {"split": "train"}
    concept_type = [ConceptType.OBJECT]