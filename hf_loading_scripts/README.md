# Notes on creating a HF dataset by writing a loading script

The dataset loading script spefifies where to download the files and how to load them into a HF dataset.

- Tutorial for writing a dataset loading script: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script; below are some related notes that might be helpful:
    - Defining the feature fields: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script
    - dataset.Value types: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script

- Upload the dataset loading script and a README file to the HF hub: https://huggingface.co/docs/datasets/share

## HF Datasets created by ourselves
- [Visual Attributes in the Wild (VAW)](vaw/)


## (TBD/Updating) Demo evaluation dataset pool
| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| OmniLabel | **object** | image | N/A | https://www.omnilabel.org/dataset/download |
| VAW | **attribute**, object | image | https://huggingface.co/datasets/mikewang/vaw | https://github.com/adobe-research/vaw_dataset#dataset-setup |
| PAD-v2 | **affordance** | image | N/A | https://github.com/lhc1224/OSAD_Net |
| ImSitu | **activity** | image | N/A | https://github.com/my89/imSitu |
| Kinetics-400 | **activity** | video | https://huggingface.co/datasets/AlexFierro9/Kinetics400 | https://www.deepmind.com/open-source/kinetics |

## (Updating) Other Ecole related datasets
| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| Visual Genome | object, attribute, relationship | image | https://huggingface.co/datasets/visual_genome | https://homes.cs.washington.edu/~ranjay/visualgenome/index.html |