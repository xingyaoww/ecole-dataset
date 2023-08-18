# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Omnilabel dataset."""


import csv
import json
import os

import datasets

_CITATION = """\
@misc{schulter2023omnilabel,
      title={OmniLabel: A Challenging Benchmark for Language-Based Object Detection},
      author={Samuel Schulter and Vijay Kumar B G and Yumin Suh and Konstantinos M. Dafnis and Zhixing Zhang and Shiyu Zhao and Dimitris Metaxas},
      year={2023},
      eprint={2304.11463},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """OmniLabel Benchmark."""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = "https://www.omnilabel.org"

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = "https://www.omnilabel.org/dataset/download#h.frhys3no2ecq"

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
# _URLS = {
#     # "first_domain": "https://huggingface.co/great-new-dataset-first_domain.zip",
#     # "second_domain": "https://huggingface.co/great-new-dataset-second_domain.zip",
# }


_URLS = {
    "val": "https://huggingface.co/datasets/xingyaoww/omnilabel/resolve/main/dataset_all_val_v0.1.3.json",
}


# TODO: Name of the dataset usually matches the script name with CamelCase instead of snake_case
class OmniLabel(datasets.GeneratorBasedBuilder):
    """TODO: Short description of my dataset."""

    VERSION = datasets.Version("1.0.0")

    # This is an example of a dataset with multiple configurations.
    # If you don't want/need to define several sub-sets in your dataset,
    # just remove the BUILDER_CONFIG_CLASS and the BUILDER_CONFIGS attributes.

    # If you need to make complex sub-parts in the datasets with configurable options
    # You can create your own builder configuration class to store attribute, inheriting from datasets.BuilderConfig
    # BUILDER_CONFIG_CLASS = MyBuilderConfig

    # You will be able to load one or the other configurations in the following list with
    # data = datasets.load_dataset('my_dataset', 'first_domain')
    # data = datasets.load_dataset('my_dataset', 'second_domain')
    # BUILDER_CONFIGS = [
    #     datasets.BuilderConfig(name="first_domain", version=VERSION, description="This part of my dataset covers a first domain"),
    #     datasets.BuilderConfig(name="second_domain", version=VERSION, description="This part of my dataset covers a second domain"),
    # ]

    # DEFAULT_CONFIG_NAME = "first_domain"  # It's not mandatory to have a default configuration. Just use one if it make sense.

    def _info(self):
        features = datasets.Features(
            {
                "id": datasets.Value("int64"),  # int (Unique instance ID)
                "image_id": datasets.Value(
                    "int64"
                ),  # the image id this annotation belongs to
                "image_filename": datasets.Value(
                    "string"
                ),  # the image filename this annotation belongs to
                "bbox": datasets.features.Sequence(
                    datasets.Value("float64")
                ),  # [x, y, width, height] (Bounding box co-ordinates for the instance)
                "descriptions": datasets.features.Sequence(
                    datasets.Value("string")
                ),  # list of the object description text
            }
        )

        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features, uncomment supervised_keys line below and
            # specify them. They'll be used if as_supervised=True in builder.as_dataset.
            # supervised_keys=("sentence", "label"),
            # Homepage of the dataset for documentation
            homepage=_HOMEPAGE,
            # License for the dataset if available
            license=_LICENSE,
            # Citation for the dataset
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        # urls = _URLS[self.config.name]
        # data_dir = dl_manager.download_and_extract(urls)

        downloaded_files = dl_manager.download_and_extract(_URLS)
        print("downloaded_files: ", downloaded_files)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": downloaded_files["val"],
                    "split": "val",
                },
            ),
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath, split):
        if split == "val":
            with open(filepath) as f:
                data = json.load(f)

            IMAGE_ID_TO_FILENAME = {}
            for image_info in data["images"]:
                IMAGE_ID_TO_FILENAME[image_info["id"]] = image_info["file_name"]

            DESCRIPTION_ID_TO_DESC = {}
            for desc in data["descriptions"]:
                DESCRIPTION_ID_TO_DESC[desc["id"]] = desc

            for key, anno in enumerate(data["annotations"]):
                image_id = anno["image_id"]
                image_filename = IMAGE_ID_TO_FILENAME[image_id]
                description_ids = anno["description_ids"]
                descriptions = [
                    DESCRIPTION_ID_TO_DESC[description_id]["text"]
                    for description_id in description_ids
                ]

                yield key, {
                    "id": anno["id"],
                    "image_id": image_id,
                    # TODO: make this a PIL.Image
                    "image_filename": image_filename,
                    "bbox": anno["bbox"],
                    "descriptions": descriptions,
                }
