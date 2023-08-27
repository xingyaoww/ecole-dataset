---
pretty_name: 'Animals with Attributes v2 (AwA2)'
language:
- en
---
# Dataset Card for Animals with Attributes v2 (AwA2)

## Dataset Description

**Homepage:** https://cvml.ista.ac.at/AwA2/

**IMPORTANT NOTES**
- This HF dataset downloads the dataset (https://cvml.ista.ac.at/AwA2/AwA2-data.zip), and loads the image instances with class-level annotations.
- The "train" split in this HF dataset contains all the images. For the original proposed splits and the proposed splits version 2.0, please refer to [here](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/zero-shot-learning/zero-shot-learning-the-good-the-bad-and-the-ugly/).
- License files is also included in the downloaded dataset (https://cvml.ista.ac.at/AwA2/AwA2-data.zip)


**Paper Citation:** 
```
@article{xian2018zero,
  title={Zero-shot learning—a comprehensive evaluation of the good, the bad and the ugly},
  author={Xian, Yongqin and Lampert, Christoph H and Schiele, Bernt and Akata, Zeynep},
  journal={IEEE transactions on pattern analysis and machine intelligence},
  volume={41},
  number={9},
  pages={2251--2265},
  year={2018},
  publisher={IEEE}
}
```

## Dataset Summary
This dataset provides a platform to benchmark transfer-learning algorithms, in particular attribute base classification and zero-shot learning [1]. It can act as a drop-in replacement to the original Animals with Attributes (AwA) dataset [2,3], as it has the same class structure and almost the same characteristics.
It consists of 37322 images of 50 animals classes with pre-extracted feature representations for each image. The classes are aligned with Osherson's classical class/attribute matrix [3,4], thereby providing 85 numeric attribute values for each class. Using the shared attributes, it is possible to transfer information between different classes.
The image data was collected from public sources, such as Flickr, in 2016. In the process we made sure to only include images that are licensed for free use and redistribution, please see the archive for the individual license files. If the dataset contains an image for which you hold the copyright and that was not licensed freely, please contact us at , so we can remove it from the collection.

**References**

[1] Y. Xian, C. H. Lampert, B. Schiele, Z. Akata. "Zero-Shot Learning - A Comprehensive Evaluation of the Good, the Bad and the Ugly", IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI) 40(8), 2018. (arXiv:1707.00600 [cs.CV])
[2] C. H. Lampert, H. Nickisch, and S. Harmeling. "Learning To Detect Unseen Object Classes by Between-Class Attribute Transfer". In CVPR, 2009
[3] C. H. Lampert, H. Nickisch, and S. Harmeling. "Attribute-Based Classification for Zero-Shot Visual Object Categorization". IEEE T-PAMI, 2013
[4] D. N. Osherson, J. Stern, O. Wilkie, M. Stob, and E. E. Smith. "Default probability". Cognitive Science, 15(2), 1991.
[5] C. Kemp, J. B. Tenenbaum, T. L. Griffiths, T. Yamada, and N. Ueda. "Learning systems of concepts with an infinite relational model". In AAAI, 2006.