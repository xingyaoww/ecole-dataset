---
pretty_name: 'imSitu dataset'
language:
- en
---
# Dataset Card for imSitu

## Dataset Description

**Homepage:** http://imsitu.org/

**Repository:** https://github.com/my89/imSitu;
- The metadata used for imSitu: https://github.com/my89/imSitu#metadata
- The images can be downloaded following: https://github.com/my89/imSitu#images
- This HF dataset loads the `train.json`, `val.json` and `test.json` from the repository

**IMPORTANT NOTE**: The `frames` field in the loaded HF dataset contains a list of json strings (since the data structure for each verb frame is different). To convert the json strings back to dicts, you can refer to the following example:
```
from datasets import load_dataset
import json
dataset = load_dataset("mikewang/imsitu")
print(dataset['train'][0])
frames = [json.loads(obj) for obj in dataset['train'][0]['frames']]
print(frames)
```

**Paper Citation:** 
```
@inproceedings{yatskar2016,
  title={Situation Recognition: Visual Semantic Role Labeling for Image Understanding},
  author={Yatskar, Mark and Zettlemoyer, Luke and Farhadi, Ali},
  booktitle={Conference on Computer Vision and Pattern Recognition},
  year={2016}
}
```

## Dataset Summary
imSitu is a dataset supporting situation recognition, the problem of producing a concise summary of the situation an image depicts including: (1) the main activity, (2) the participating actors, objects, substances, and locations and most importantly (3) the roles these participants play in the activity. The role set used by imSitu is derived from the linguistic resource FrameNet and the entities are derived from ImageNet. The data in imSitu can be used to create robust algorithms for situation recongntion.