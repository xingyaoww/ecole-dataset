# Notes on creating a HF dataset by writing a loading script

The dataset loading script spefifies where to download the files and how to load them into a HF dataset.

- Tutorial for writing a dataset loading script: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script; below are some related notes that might be helpful:
    - Defining the feature fields: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script
    - dataset.Value types: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script

- Upload the dataset loading script and a README file to the HF hub: https://huggingface.co/docs/datasets/share

## Implemented Datasets

- [Visual Attributes in the Wild (VAW)](vaw/)