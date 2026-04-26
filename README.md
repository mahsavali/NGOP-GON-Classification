# 👁️ NGON vs. GON Classification & Optic Disk Segmentation

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Distinguishing Non-Glaucomatous Optic Neuropathy (**NGON**) from Glaucomatous Optic Neuropathy (**GON**) based on optic disc appearance can be challenging, as both can have similar characteristics. This repository provides a deep-learning framework to automate this differentiation with high precision.

## 🚀 Research Summary
The goal of this research was to evaluate a deep-learning system's ability to distinguish between GON and NGON using fundus images. 
* **Model:** DenseNet121
* **Training Performance:** 95.36% Sensitivity and 97.63% Specificity.
* **External Testing:** Overall precision of 86.07%, indicating high generalizability.
* **Clinical Impact:** The deep learning method showed significantly better sensitivity (85.53%) compared to glaucoma specialists.

## 🔬 Methodology
Our framework employs a two-stage pipeline:
1.  **Segmentation (OD-SEG):** Using a modified **U-Net** model for Region of Interest (ROI) and optic disc segmentation.
2.  **Classification:** Utilizing **DenseNet121** for its efficient feature transfer via dense connections, allowing the model to capture fine-grained pathological details.

![Figure1300](https://user-images.githubusercontent.com/119206364/205449245-f4072bac-d2fa-4dc0-a020-698f8b68adac.jpg)
*Figure Overview: (A) Automated classification pipeline, (B) Healthy/GON/NGON examples, (C) Framework steps, (D) OD-SEG and Transfer Learning architecture.*

## 📂 Project Structure
* `OpticDiskSegmentation.ipynb`: Training the U-Net for OD segmentation.
* `predicfundusseg.py`: Inference script for segmenting the Optic Disk from fundus images.
* `K-Fold.ipynb`: Robust training/evaluation using K-Fold cross-validation.
* `DataSplit.ipynb`: Data orchestration and train/test partitioning.
* `Metrics.py`: Custom module for medical metrics (Specificity, Sensitivity, F1-Score).

## 🚀 Getting Started

### Installation
```bash
pip install tensorflow opencv-python matplotlib scikit-learn scikit-image tqdm



## 💻Usage
To predict the segmentation mask for an image:
```bash
Python
python predicfundusseg.py
```
📝Citation
If you use this code or research in your work, please cite it as follows:

Code snippet
@article{vali2023differentiating,
  title={Differentiating glaucomatous optic neuropathy from non-glaucomatous optic neuropathies using deep learning algorithms},
  author={Vali, Mahsa and Mohammadi, Massood and Zarei, Nasim and Samadi, Melika and Atapour-Abarghouei, Amir and others},
  journal={American journal of ophthalmology},
  volume={252},
  pages={1--8},
  year={2023},
  publisher={Elsevier}
}
⭐ Show some love!
Is this repo helping you save the world's eyesight? Or did it just save you from a coding headache? 🤕

Either way, if you found this useful, hit that Star button! It’s free, it makes the AI happy, and it's 100% more effective than a "get well soon" card for your code. 🌟🚀

Developed with ❤️ for Medical AI Advancement.
