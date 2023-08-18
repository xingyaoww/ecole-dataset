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

"""imSitu dataset"""


import csv
import json
import os

import datasets

_CITATION = """\
@inproceedings{yatskar2016,
  title={Situation Recognition: Visual Semantic Role Labeling for Image Understanding},
  author={Yatskar, Mark and Zettlemoyer, Luke and Farhadi, Ali},
  booktitle={Conference on Computer Vision and Pattern Recognition},
  year={2016}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
imSitu is a dataset supporting situation recognition, the problem of producing a concise summary of the situation an image depicts including: (1) the main activity, (2) the participating actors, objects, substances, and locations and most importantly (3) the roles these participants play in the activity. The role set used by imSitu is derived from the linguistic resource FrameNet and the entities are derived from ImageNet. The data in imSitu can be used to create robust algorithms for situation recongntion.

Repository: https://github.com/my89/imSitu;
- The metadata used for imSitu: https://github.com/my89/imSitu#metadata
- The images can be downloaded following: https://github.com/my89/imSitu#images
- This HF dataset loads the `train.json`, `val.json` and `test.json` from the repository
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = "http://imsitu.org/"

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
# _URLS = {
#     # "first_domain": "https://huggingface.co/great-new-dataset-first_domain.zip",
#     # "second_domain": "https://huggingface.co/great-new-dataset-second_domain.zip",
# }

_URL = "https://raw.githubusercontent.com/my89/imSitu/master/"
_URLS = {
    "train": _URL + "train.json",
    "val": _URL + "dev.json",
    "test": _URL + "test.json"
}


# TODO: Name of the dataset usually matches the script name with CamelCase instead of snake_case
class imSitu(datasets.GeneratorBasedBuilder):
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
                "image_id": datasets.Value("string"), # int (Image ids correspond to respective Visual Genome image ids)
                "frames":datasets.features.Sequence(datasets.Value("string")), # list of jsonl strings indicating frames
                "verb": datasets.Value("string"),
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
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": downloaded_files["train"],
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": downloaded_files["val"],
                    "split": "val",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": downloaded_files["test"],
                    "split": "test"
                },
            ),
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath, split):
        # TODO: This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        # The `key` is for legacy reasons (tfds) and is not important in itself, but must be unique for each example.
        # with open(filepath, encoding="utf-8") as f:
        #     for key, row in enumerate(f):
        #         data = json.loads(row)
        #         if self.config.name == "first_domain":
        #             # Yields examples as (key, example) tuples
        #             yield key, {
        #                 "sentence": data["sentence"],
        #                 "option1": data["option1"],
        #                 "answer": "" if split == "test" else data["answer"],
        #             }
        #         else:
        #             yield key, {
        #                 "sentence": data["sentence"],
        #                 "option2": data["option2"],
        #                 "second_domain_answer": "" if split == "test" else data["second_domain_answer"],
        #             }
    
        data = json.load(open(filepath, encoding="utf-8"))

        for key, row in data.items():
            yield key, {
                "image_id": key,
                "frames": [json.dumps(obj) for obj in row["frames"]],
                "verb": row["verb"]
            }
