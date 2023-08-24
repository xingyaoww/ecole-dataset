---
pretty_name: 'Padv2 Dataset - Part1'
language:
- en
---
# Dataset Card for Padv2 Part1

## Dataset Description

**Official Repo:** https://github.com/lhc1224/OSAD_Net#-dataset-;

**IMPORTANT Notes**:
- This Huggingface dataset loads the Part1 of the Padv2 dataset, i.e., the PADv2_part1.zip; The file can also be downloaded from: https://uofi.box.com/s/1atjh3d2p82qyxm3gp11514006va0llq
- Each instance in the loaded HF dataset contains the following fields: 
    - `image_uid`: unique id to a dataset instanec
    - `image_path`: path to the raw rgb image
    - `depth_path`: path to the depth annotation of the image
    - `mask_path`: path to the object mask of the image
    - `affordance_type`: affordance type of the object in the image
    - `original_divisions`: there are three versions of divisions on the affordance types in the original dataset, this field stores the split ("train" or "test") of this instance in the three different divisions ("divide_1", "divide_2", "divide_3")


**Paper Citation:** 
```
@inproceedings{Oneluo,
  title={One-Shot Affordance Detection},
  author={Hongchen Luo and Wei Zhai and Jing Zhang and Yang Cao and Dacheng Tao},
  booktitle={IJCAI},
  year={2021}
}
```
```
@article{luo2021one,
  title={One-Shot Object Affordance Detection in the Wild},
  author={Zhai, Wei and Luo, Hongchen and Zhang, Jing and Cao, Yang and Tao, Dacheng},
  journal={arXiv preprint arXiv:2108.03658},
  year={2021}
}
```
## Dataset Summary
With complex scenes and rich annotations, the PADv2 dataset can be used as a test bed to benchmark affordance detection methods and may also facilitate downstream vision tasks, such as scene understanding, action recognition, and robot manipulation.

It contains 30k diverse images covering 39 affordance categories as well as 103 object categories from different scenes.