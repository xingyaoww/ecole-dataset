---
pretty_name: 'Visual Attributes in the Wild (VAW)'
language:
- en
---
# Dataset Card for Visual Attributes in the Wild (VAW)

## Dataset Description

**Homepage:** http://vawdataset.com/

**Repository:** https://github.com/adobe-research/vaw_dataset;
- The raw dataset files will be downloaded from: https://github.com/adobe-research/vaw_dataset/tree/main/data, where one can also find additional metadata files such as attribute types. 
- The train split loaded from this hf dataset is a concatenation of the train_part1.json and train_part2.json. 
- The image_id field corresponds to respective image ids in the v1.4 Visual Genome dataset.

**LICENSE:** https://github.com/adobe-research/vaw_dataset/blob/main/LICENSE.md

**Paper Citation:** 
```
@InProceedings{Pham_2021_CVPR,
    author    = {Pham, Khoi and Kafle, Kushal and Lin, Zhe and Ding, Zhihong and Cohen, Scott and Tran, Quan and Shrivastava, Abhinav},
    title     = {Learning To Predict Visual Attributes in the Wild},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {13018-13028}
}
```

## Dataset Summary
A large scale visual attributes dataset with explicitly labelled positive and negative attributes.

- 620 Unique Attributes including color, shape, texture, posture and many others
- 260,895 Instances of different objects
- 2260 Unique Objects observed in the wild
- 72,274 Images from the Visual Genome Dataset
- 4 different evaluation metrics for measuring multi-faceted performance metrics