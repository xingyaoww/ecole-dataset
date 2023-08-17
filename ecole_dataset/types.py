from collections import namedtuple


# kwargs is a dict of keyword arguments to pass to the dataset.map function
# https://huggingface.co/docs/datasets/v2.14.4/en/package_reference/main_classes#datasets.Dataset.map
PreprocessorType = namedtuple(
    "Preprocessor",
    ["function", "kwargs"]
)
