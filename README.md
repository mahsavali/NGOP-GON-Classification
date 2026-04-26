# 👁️ NGON vs. GON Classification & Optic Disk Segmentation

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow 2.x](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Distinguishing Non-Glaucomatous Optic Neuropathy (**NGON**) from Glaucomatous Optic Neuropathy (**GON**) based on optic disc appearance is clinically challenging due to overlapping characteristics. This project implements a high-performance AI pipeline to automate this differentiation using fundus images.

## 📝 Research Summary
The goal of this research was to evaluate a deep-learning system's ability to distinguish between GON and NGON. The **DenseNet121** model demonstrated superior performance:
* **Sensitivity:** 95.36% (Training)
* **Specificity:** 97.63% (Training)
* **External Precision:** 86.07% (Generalizability)
* **Clinical Comparison:** The model achieved significantly better sensitivity (85.53%) compared to glaucoma specialists in external testing.

## 🔬 Methodology & Architecture
The framework follows a two-stage process:
1.  **OD-SEG Network:** A modified **U-Net** model is used for Region of Interest (ROI) and Optic Disc (OD) segmentation to isolate the relevant area.
2.  **Classification:** Transfer Learning with **DenseNet121**. This architecture was chosen for its dense connectivity, which enhances feature transfer across different granularity levels.

![Figure1300](https://user-images.githubusercontent.com/119206364/205449245-f4072bac-d2fa-4dc0-a020-698f8b68adac.jpg)
*Figure: (A) Proposed method view, (B) Disease examples, (C) Framework steps, (D) OD-SEG & Transfer Learning architecture.*

## 📂 Repository Structure
* `OpticDiskSegmentation.ipynb`: Implementation and training of the U-Net segmentation model.
* `predicfundusseg.py`: Script for loading the trained model and predicting segmentation masks on new images.
* `K-Fold.ipynb`: Implementation of K-Fold cross-validation to ensure model stability and robustness.
* `DataSplit.ipynb`: Preprocessing steps, including data loading and train/test splitting.
* `Metrics.py`: Custom evaluation functions (Sensitivity, Specificity, Confusion Matrix).

## 🚀 Getting Started

### Prerequisites
```bash
pip install tensorflow opencv-python matplotlib scikit-learn scikit-image tqdm
