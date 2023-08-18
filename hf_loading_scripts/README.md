## Notes on creating a HF dataset by writing a loading script

The dataset loading script spefifies where to download the files and how to load them into a HF dataset.

- Tutorial for writing a dataset loading script: https://huggingface.co/docs/datasets/dataset_script#create-a-dataset-loading-script; below are some related notes that might be helpful:
    - Defining the feature fields: https://huggingface.co/docs/datasets/about_dataset_features
    - dataset.Value types: https://huggingface.co/docs/datasets/v2.14.4/en/package_reference/main_classes#datasets.Value

- Upload the dataset loading script and a README file to the HF hub: https://huggingface.co/docs/datasets/share

## HF Datasets created by ourselves
- [Visual Attributes in the Wild (VAW)](vaw/)
- [imSitu](imsitu/)


## (TBD|Updating) Demo evaluation dataset pool
| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| OmniLabel | **object** | image | N/A | https://www.omnilabel.org/dataset/download |
| VAW | **attribute**, object | image | https://huggingface.co/datasets/mikewang/vaw | https://github.com/adobe-research/vaw_dataset#dataset-setup |
| PAD-v2 | **affordance** | image | N/A | https://github.com/lhc1224/OSAD_Net |
| ImSitu | **activity** | image | https://huggingface.co/datasets/mikewang/imsitu | https://github.com/my89/imSitu |
| Kinetics-400 | **activity** | video | https://huggingface.co/datasets/AlexFierro9/Kinetics400 | https://www.deepmind.com/open-source/kinetics |

## (Updating) Other Ecole related datasets
| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| Visual Genome | object, attribute, relationship | image | https://huggingface.co/datasets/visual_genome | https://homes.cs.washington.edu/~ranjay/visualgenome/index.html |


## [Updated Aug18] Implementation Notes
- Done converting HF datasets: VAW, ImSitu
- TODO: Padv2
    - Downloaded and unziped Padv2 dataset: /shared/nas/data/m1/shared-resource/vision-language/data/raw/Padv2
- TODO: Add instruction/implementation handling image downloading