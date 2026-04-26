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

## 🎯 Key Contributions

- ✅ End-to-end **two-stage deep learning pipeline**
- 🧠 Integration of **U-Net (segmentation)** and **DenseNet121 (classification)**
- 📈 Clinically relevant evaluation using **Sensitivity & Specificity**
- 🌍 Demonstrated **generalization on external datasets**
- 🏥 Performance surpassing human glaucoma specialists in sensitivity

---

## 📊 Performance Summary

| Metric                  | Value        |
|------------------------|-------------|
| **Sensitivity (Train)** | 95.36%      |
| **Specificity (Train)** | 97.63%      |
| **External Precision**  | 86.07%      |
| **Clinical Sensitivity**| 85.53% (↑ vs Specialists) |

---

## 🧠 Methodology

### 🔹 Stage 1: Optic Disc Segmentation (OD-SEG)
- Architecture: **Modified U-Net**
- Purpose: Extract **Region of Interest (ROI)**  
- Output: Precise optic disc mask for downstream classification  

### 🔹 Stage 2: Classification
- Architecture: **DenseNet121**
- Key Advantage:  
  - Efficient **feature reuse via dense connections**
  - Improved learning of **fine-grained pathological patterns**

---

## 🖼️ System Pipeline

![Framework](https://user-images.githubusercontent.com/119206364/205449245-f4072bac-d2fa-4dc0-a020-698f8b68adac.jpg)

---

## 🏗️ Project Architecture

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


Either way, if you found this useful, hit that Star button! It’s free, it makes the AI happy, and it's 100% more effective than a "get well soon" card for your code. 🌟🚀

Developed with ❤️ for Medical AI Advancement.
