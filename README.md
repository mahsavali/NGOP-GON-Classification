# NGOP-GON-Classification
Distinguishing NGON from GON based on optic disc appearance can be challenging, as both can have similar characteristics. Previous studies have highlighted this difficulty. The AI approach in this study has been effective in this regard.
# Research Summary
The research aimed to evaluate a deep-learning system's ability to distinguish between Glaucomatous Optic Neuropathy (GON) and Non-Glaucomatous Optic Neuropathy (NGON) using fundus images. The DenseNet121 model demonstrated high performance with a sensitivity of 95.36% and specificity of 97.63% in the training dataset. In external testing, the network had an overall precision of 86.07%, indicating its generalizability. When compared to a glaucoma specialist, the deep learning method showed significantly better sensitivity (85.53%).

## Methodology
In the comparison with previous work, this research used a modified U-net model for region of interest (ROI) and disc segmentation, included a larger dataset with more GON and NGON cases, and tested various convolutional neural networks (CNNs). DenseNet121 performed the best due to its connections between different layers, allowing for better feature transfer at different granularity levels.
"The figure below illustrates: (A) A general view of the proposed method for automated fundus image classification, (B) Examples from healthy, GON, and NGON fundus images, (C) Steps of the proposed framework, and (D) OD-SEG network and Transfer Learning architecture."
![Figure1300](https://user-images.githubusercontent.com/119206364/205449245-f4072bac-d2fa-4dc0-a020-698f8b68adac.jpg)

## Conclusion
The study acknowledges limitations, including the relatively small size of the external dataset and the fact that the glaucoma specialist differentiated only between GON and NGON in external data. Nonetheless, the deep learning model outperformed the specialist, indicating its potential in assisting ophthalmologists, glaucoma specialists, and neuro-ophthalmologists in accurately distinguishing GON from NGON for appropriate management.

## Related Research

- [Link to the Research Paper]([https://example.com/paper.pdf](https://www.sciencedirect.com/science/article/abs/pii/S000293942300082X)https://www.sciencedirect.com/science/article/abs/pii/S000293942300082X)
