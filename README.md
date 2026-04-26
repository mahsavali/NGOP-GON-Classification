# 👁️ NGON vs. GON Classification & Optic Disc Segmentation  
### Deep Learning Framework for Automated Ophthalmic Diagnosis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Status](https://img.shields.io/badge/Status-Research%20Ready-success.svg)]()  
[![Domain](https://img.shields.io/badge/Domain-Medical%20AI-critical)]()  

---

## 📌 Abstract

Differentiating **Glaucomatous Optic Neuropathy (GON)** from **Non-Glaucomatous Optic Neuropathy (NGON)** remains a critical and challenging task in clinical ophthalmology due to overlapping visual biomarkers in fundus imaging.

This repository introduces a **robust deep learning pipeline** that integrates **optic disc segmentation** and **disease classification** to achieve high diagnostic accuracy and strong generalization across datasets.

---

## 🧪 Technical Summary

This project is based on a deep learning framework designed to differentiate 
Glaucomatous Optic Neuropathy (GON) from Non-Glaucomatous Optic Neuropathy (NGON) 
using color fundus images.

The model was trained on 2,183 labeled fundus images and evaluated on multiple 
external datasets to ensure generalizability. The pipeline incorporates optic 
disc segmentation followed by transfer learning-based classification.

The best-performing model (DenseNet121) achieved high diagnostic performance, 
with strong sensitivity and specificity, and demonstrated superior sensitivity 
compared to glaucoma specialists in external validation.

---

## 🎯 Key Contributions

- End-to-end two-stage deep learning pipeline  
- Integration of U-Net (segmentation) and DenseNet121 (classification)  
- Clinically relevant evaluation (Sensitivity, Specificity)  
- Strong generalization on external datasets  
- Performance surpassing glaucoma specialists in sensitivity  

---

## 📊 Performance Summary

| Metric                  | Value        |
|------------------------|-------------|
| Sensitivity (Train)    | 95.36%      |
| Specificity (Train)    | 97.63%      |
| External Precision     | 86.07%      |
| Clinical Sensitivity   | 85.53%      |

---

## 🧠 Methodology

### Stage 1: Optic Disc Segmentation (OD-SEG)
- Modified U-Net  
- ROI extraction  

### Stage 2: Classification
- DenseNet121  
- Dense feature reuse for fine-grained learning  

---

## 🖼️ Pipeline

![Framework](https://user-images.githubusercontent.com/119206364/205449245-f4072bac-d2fa-4dc0-a020-698f8b68adac.jpg)

---

## 🏗️ Project Structure

```
.
├── OpticDiskSegmentation.ipynb
├── predicfundusseg.py
├── K-Fold.ipynb
├── DataSplit.ipynb
├── Metrics.py
```

---

## ⚙️ Installation

```
pip install tensorflow opencv-python matplotlib scikit-learn scikit-image tqdm
```

---

## 🚀 Usage

```
python predicfundusseg.py
```

---

## 📚 Citation

```
@article{vali2023differentiating,
  title={Differentiating glaucomatous optic neuropathy from non-glaucomatous optic neuropathies using deep learning algorithms},
  author={Vali, Mahsa and others},
  journal={American Journal of Ophthalmology},
  year={2023}
}
```

---

## 📜 License

MIT License
