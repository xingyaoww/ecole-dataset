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

"""Padv2 dataset Part1"""


import csv
import json
import os

import datasets
import requests
from tqdm import tqdm
from zipfile import ZipFile
from collections import defaultdict

_CITATION = """\
@article{luo2021one,
  title={One-Shot Object Affordance Detection in the Wild},
  author={Zhai, Wei and Luo, Hongchen and Zhang, Jing and Cao, Yang and Tao, Dacheng},
  journal={arXiv preprint arXiv:2108.03658},
  year={2021}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
Padv2 dataset:https://github.com/lhc1224/OSAD_Net#-dataset-;
- This dataset loads the PADv2_part1.zip
- Each instance contains the following fields: 
    - `image_uid`: unique id to a dataset instanec
    - `image_path`: path to the raw rgb image
    - `depth_path`: path to the depth annotation of the image
    - `mask_path`: path to the object mask of the image
    - `affordance_type`: affordance type of the object in the image
    - `original_divisions`: there are three versions of divisions on the affordance types in the original dataset, this field stores the split ("train" or "test") of this instance in the three different divisions ("divide_1", "divide_2", "divide_3")
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = "https://github.com/lhc1224/OSAD_Net#-dataset-"

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
# _URLS = {
#     # "first_domain": "https://huggingface.co/great-new-dataset-first_domain.zip",
#     # "second_domain": "https://huggingface.co/great-new-dataset-second_domain.zip",
# }


_URLS = {
    "val": "https://uofi.box.com/shared/static/1atjh3d2p82qyxm3gp11514006va0llq.zip" # original division and split info are stored in the "original_divisions" field for each instance
}


def _load_padv2_part1_instances(Padv2_part1_unzipped_root):
    data = defaultdict(lambda: {
        "image_path": None,
        "depth_path": None,
        "mask_path": None,
        "affordance_type": None,
        "original_divisions": {
            "divide_1": None,
            "divide_2": None,
            "divide_3": None
        }
    })

    for division in ["divide_1", "divide_2", "divide_3"]:
        for split in ["train", "test"]:
            split_dir = os.path.join(Padv2_part1_unzipped_root, division, split)
            image_dir = os.path.join(split_dir, "images")
            mask_dir = os.path.join(split_dir, "masks")
            depth_dir = os.path.join(split_dir, "depth")
            for affordance_type in os.listdir(image_dir):
                affordance_type_dir = os.path.join(image_dir, affordance_type)
                for object_type in os.listdir(affordance_type_dir):
                    object_type_dir = os.path.join(affordance_type_dir, object_type)
                    for image_name_with_extension in os.listdir(object_type_dir):
                        image_name = image_name_with_extension.split(".")[0]
                        image_uid = f"{affordance_type}__{object_type}__{image_name}"
                        assert len(image_uid.split("__")) == 3
                        if data[image_uid]["image_path"] is None:
                            data[image_uid]["image_path"] = os.path.join(object_type_dir, image_name_with_extension)
                            data[image_uid]["depth_path"] = os.path.join(depth_dir, affordance_type, object_type, image_name + ".png")
                            data[image_uid]["mask_path"] = os.path.join(mask_dir, affordance_type, object_type, image_name + ".png")
                            data[image_uid]["affordance_type"] = affordance_type
                        data[image_uid]["original_divisions"][division] = split
    return data

def _download_box_file(url, destination):
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # Adjust the block size as needed
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    with open(destination, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()
    print("Download completed!")

# TODO: Name of the dataset usually matches the script name with CamelCase instead of snake_case
class PadV2(datasets.GeneratorBasedBuilder):
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
        # TODO: This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset
        # if self.config.name == "first_domain":  # This is the name of the configuration selected in BUILDER_CONFIGS above
        #     features = datasets.Features(
        #         {
        #             "sentence": datasets.Value("string"),
        #             "option1": datasets.Value("string"),
        #             "answer": datasets.Value("string")
        #             # These are the features of your dataset like images, labels ...
        #         }
        #     )
        # else:  # This is an example to show how to have different features for "first_domain" and "second_domain"
        #     features = datasets.Features(
        #         {
        #             "sentence": datasets.Value("string"),
        #             "option2": datasets.Value("string"),
        #             "second_domain_answer": datasets.Value("string")
        #             # These are the features of your dataset like images, labels ...
        #         }
        #     )

        features = datasets.Features(
            {
                "image_uid": datasets.Value("string"), 
                "image_path": datasets.Value("string"),
                "depth_path": datasets.Value("string"),
                "mask_path": datasets.Value("string"),
                "affordance_type": datasets.Value("string"),
                "original_divisions": {
                    "divide_1": datasets.Value("string"),
                    "divide_2": datasets.Value("string"),
                    "divide_3": datasets.Value("string")
                }
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

        cache_dir = dl_manager.download_config.cache_dir # use the huggingface cache dir
        zip_file_path = os.path.join(cache_dir, "PADv2_part1.zip")

        # download the zip file from Box if not exist
        if not os.path.exists(zip_file_path):
            print("downloading to:", zip_file_path)
            _download_box_file(_URLS["val"], zip_file_path)
        
        # unzip folder if not exist
        Padv2_part1_unzipped_root = os.path.join(os.path.dirname(zip_file_path), "extracted", "PADv2_part1")
        if not os.path.exists(Padv2_part1_unzipped_root):
            print("unzipping to:", Padv2_part1_unzipped_root)
            with ZipFile(zip_file_path, 'r') as zObject:
                zObject.extractall(path=os.path.dirname(Padv2_part1_unzipped_root))

        downloaded_files = {'val': os.path.join(Padv2_part1_unzipped_root)}
        # downloaded_files = dl_manager.download_and_extract(_URLS)
        print("downloaded_files:", downloaded_files)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": downloaded_files["val"],
                    "split": "val",
                },
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath, split):
        # TODO: This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        # The `key` is for legacy reasons (tfds) and is not important in itself, but must be unique for each example.

        # the filepath points to the unzipped Padv2_part1 folder
        if split == "val":
            data = _load_padv2_part1_instances(filepath)
            for key, row in data.items():
                yield key, {
                    "image_uid": key, 
                    "image_path": row['image_path'],
                    "depth_path": row['depth_path'],
                    "mask_path": row['mask_path'],
                    "affordance_type": row['affordance_type'],
                    "original_divisions": row['original_divisions']
                }