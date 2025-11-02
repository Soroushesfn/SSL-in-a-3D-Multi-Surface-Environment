<!-- PROJECT LOGO -->
<table width="100%">
  <tr>
    <td align="left" width="10%">
      <img src="./Images/taarlab.png" alt="Left Logo" width="120" />
    </td>
    <td align="center" width="80%">
      <h1 style="margin:0; padding:0;">SSL-in-a-3D-Multi-Surface-Environment</h1>
    </td>
    <td align="right" width="10%">
      <img src="./Images/UT.png" alt="Right Logo" width="120" />
    </td>
  </tr>
</table>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#repository-structure">Repository Structure</a></li>
    <li><a href="#experimental-setup">Experimental Setup</a></li>
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#results-summary">Results Summary</a></li>
    <li><a href="#insight-and-conclusion">Insight and Conclusion
</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#authors">Authors</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
In this research work, **Sound Source Localization using Cost-effective devices in a 3-Dimensional Multi-Surface Environment** was investigated and several Machine Learning and Deep Learning methods, including Multi-Branch Deep Neural Networks were employed in order to automate the task of Sound Source Localization and their performance were compared to the classical TDOA metods.

For this purpose, two main methods are proposed, namely **Region** and **Surface** **Classification** methods, where results demonstrate that the two proposed methods
 improve the localization performance across various scenarios,
 with the region classification method significantly outperforming
 the baseline method, achieving a 17% reduction in the Mean
 Euclidean Distance error metric. Furthermore, the surface and
 region classification methods reduce the localization time com
pared to the baseline method by 50% and 97%, respectively.
 The obtained results reveal the potential of combining simple
 learning-based models with affordable microphone sensors for
 achieving an accurate localization of sparse audio samples in a
 multi-surface environment.

The paper is published in an IEEE-indexed conference and can be accessed [Here](https://ieeexplore.ieee.org/document/10903645) and is provided in this current repository as well. After explaining the structure of the repo, the main sections of the performed work are briefly elaborated.

## Repository Structure


## Experimental Setup

The experiments were conducted in a **3D multi-surface environment** (2.82 × 4 × 0.75 m) inside the Human and Robot Interaction Lab, University of Tehran.  
Two primary surfaces were considered:
- **Ground:** artificial grass layer  
- **Table:** wooden surface (1.1 × 0.7 × 0.75 m)

Three **Microsoft Kinect v1** sensors (K1, K2, K3) were used for audio acquisition, each equipped with **4 synchronized microphones** sampling at 16 kHz.  
Kinect centers were placed at:
```
K1 → (2.82, 2.0, 0.75) m
K2 → (1.4, 0.0, 0.05) m
K3 → (0.0, 2.0, 0.75) m
```
Devices were *not inter-synchronized*, adding realism to the dataset.

A total of **315 spatial locations** (28 on table + 287 on ground) were defined at 20 cm intervals.  
At each point, a **ball-drop sound** was replayed through a **Bose SoundLink Color II** speaker, using recordings of real drops collected by a smartphone 5 cm away from impact.  
Samples were denoised via **spectral subtraction** and zero-padded to 9.06 s (145 k samples).  
The environment’s **SNR ≈ 15.3 dB** and **RT60 ≈ 0.6 s**.

## Methodology

### 1️. Classical Baseline
- **TDOA estimation:** via *GCC-PHAT* across all microphone pairs (6 per Kinect).  
- **Localization:** Gaussian-likelihood search on a 1 cm-resolution 3D grid.  
- The point with the maximum likelihood was selected as the predicted location.  

### 2️. Learning-Based Surface Classification
- Classifies whether the impact occurred on **Ground** or **Table** using GCC-PHAT-derived TDOA features.  
- Models: **Random Forest, Gradient Boosting, SVM, XGBoost.**  
- The classical algorithm then searches **only within the predicted surface**, halving computation time.

### 3️. Learning-Based Region Classification
- Environment divided into **20 regions** (18 ground + 2 table).  
- Predicts the region of impact before applying the classical search within that sub-region.  
- Models used:  
  - Simple: Random Forest, Gradient Boosting, SVM, XGBoost  
  - Deep: multi-branch MLP and CNN architectures combining TDOA, power spectrum, and phase spectrum inputs.  
- Each branch processes Kinect-specific features; outputs concatenated through dense layers for region prediction.

---

## Results Summary

| Method | Best Setup | MED (cm) ↓ | Improvement vs Baseline | Avg Time ↓ |
|:--|:--|:--|:--|:--|
| **Classical (GCC-PHAT)** | K2 + K3 | 28.4 cm | — | 29.8 s |
| **Surface Classification + XGBoost** | K2 + K3 | 28.4 cm | ≈ same accuracy | 14.7s (-50 %) |
| **Region Classification + Random Forest** | K2 + K3 | 23.4 cm | -17% error | 0.71s (-97 %) |

**Key Findings**
- *Region classification* dramatically reduces computation time while improving accuracy.  
- Simple models (Random Forest & XGBoost) outperformed deeper architectures due to the limited dataset size.  
- The **K2 + K3 configuration** proved optimal; including K1 degraded performance slightly.  
- Removing the closest-mic TDOA (TClose2) further reduced MED by ~0.5 cm.  
- Visual results show robust localization across regions, except minor occlusions behind the table.

---

## Insight and Conclusion
This work shows that **cost-effective microphone arrays** and **simple learning-based models** can achieve robust 3D sound localization in reverberant, multi-surface environments.  
The final region-classification framework achieved **17 % higher accuracy** and **97 % faster inference** than the classical baseline — demonstrating a practical path for low-cost SSL systems in robotics.



<!-- LICENSE -->
## License

Distributed under the Apache License 2.0 License. See `LICENSE` for more information.


<!-- Authors -->
## Authors

Soroush Esfahanian - Soroush.Esfahanian83@gmail.com\
Project Link: [https://github.com/Soroushesfn/SSL-in-a-3D-Multi-Surface-Environment](https://github.com/Soroushesfn/SSL-in-a-3D-Multi-Surface-Environment)