## [Update Oct 10] New datasets to be considered
- iNaturalist (2021): https://github.com/visipedia/inat_comp/tree/master/2021
- FGVC workshop: https://sites.google.com/view/fgvc8/home
- OVEN: https://open-vision-language.github.io/oven/
- Dollar street dataset: https://www.gapminder.org/dollar-street
- GeoDE: https://geodiverse-data-collection.cs.princeton.edu/

# Quickstart

Install the ECOLE dataset package.

```bash
pip3 install git+https://github.com/xingyaoww/ecole-dataset.git
```

For example, you can load all the evaluation datasets by running the following code:

```python
import ecole_dataset
test_datasets = ecole_dataset.registry.load_datasets(
    split=ecole_dataset.SplitType.TEST
)
```

Please check `scripts/example_usecase.ipynb` for more examples.

NOTE: This package currently only supports loading dataset metadata (i.e., the `test_datasets` returned by `.load_datasets` does not contains pre-loaded images, but only image filepaths). We are actively working on allowing images to be also automatically loaded into `test_datasets` with a single line of code.

Please refer to [docs/IMAGE_DATA.md](docs/IMAGE_DATA.md) to learn about how to download images and configure so that `ecole-dataset` can automatically loads images with one line of code.


## Currently Supported Evaluation Datasets

| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| OmniLabel | **object** | image | https://huggingface.co/datasets/xingyaoww/omnilabel | https://www.omnilabel.org/dataset/download |
| VAW | **attribute**, object | image | https://huggingface.co/datasets/mikewang/vaw | https://github.com/adobe-research/vaw_dataset#dataset-setup |
| PAD-v2 | **affordance** | image | https://huggingface.co/datasets/mikewang/padv2 | https://github.com/lhc1224/OSAD_Net |
| ImSitu | **activity** | image | https://huggingface.co/datasets/mikewang/imsitu | https://github.com/my89/imSitu |
| Kinetics-400 | **activity** | video | https://huggingface.co/datasets/AlexFierro9/Kinetics400 | https://www.deepmind.com/open-source/kinetics |
| AwA2 | **attribute** (Animal) | image | https://huggingface.co/datasets/mikewang/AwA2 | https://cvml.ista.ac.at/AwA2/ |
| EuroSAT | **object** (Satellite Imagery) | image | https://huggingface.co/datasets/mikewang/EuroSAT | https://github.com/phelber/EuroSAT |

## Currently Supported Other Datasets

| Datasets | Concept Types | Format | HF Dataset Link | Official Repo/Homepage |
|----------|----------|----------|----------|----------|
| Visual Genome | object, attribute, relationship | image | https://huggingface.co/datasets/visual_genome | https://homes.cs.washington.edu/~ranjay/visualgenome/index.html |
