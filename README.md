# 🎬 MovieMatch AI

## Personalized Movie Recommendation System using LightFM

![Python](https://img.shields.io/badge/Python-3.13-orange?logo=python)
![LightFM](https://img.shields.io/badge/Model-LightFM-ec4899)
![Dataset](https://img.shields.io/badge/Dataset-MovieLens%20100K-f97316)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b?logo=streamlit)

---

## 📌 Project Overview

MovieMatch AI is a personalized movie recommendation system developed using **LightFM** and the **MovieLens 100K** dataset.

The project transforms ratings of 4 and 5 into positive user-item interactions, trains a LightFM model using **WARP loss**, evaluates ranking performance, and generates top-N movie recommendations.

The deployed Streamlit application uses precomputed recommendation outputs for faster and more stable cloud deployment.

---

## ✨ Features

- Personalized recommendations for 943 users
- Adjustable top-N recommendation output
- User profile display
- Popular and highly rated movie exploration
- Rating-distribution analysis
- User-activity analytics
- Model-performance dashboard
- Downloadable recommendation CSV files
- Cinematic orange and pink interface

---

## 📂 Dataset

**Dataset:** MovieLens 100K

| Data | Count |
|---|---:|
| Users | 943 |
| Movies | 1,682 |
| Ratings | 100,000 |
| Positive Interactions | 55,375 |

Ratings of **4 and 5** were treated as positive user preferences.

---

## 🧠 Final Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | LightFM |
| Loss Function | WARP |
| Latent Components | 50 |
| Learning Rate | 0.03 |
| Epochs | 40 |
| Threads | 1 |

---

## 📈 Final Evaluation Results

| Metric | Score |
|---|---:|
| Train Precision@10 | **59.42%** |
| Test Precision@10 | **21.77%** |
| Test Recall@10 | **24.62%** |
| Test AUC | **93.99%** |

The Test AUC of approximately **0.94** shows strong ranking capability.

---

## 📁 Project Structure

```text
LightFM-Recommendation-System/
├── Application.py
├── Recommendation_System.ipynb
├── requirements.txt
├── README.md
├── models/
│   ├── lightfm_model.pkl
│   ├── train_interactions.pkl
│   ├── user_id_map.pkl
│   ├── item_id_map.pkl
│   ├── reverse_item_id_map.pkl
│   ├── model_metrics.pkl
│   ├── user_recommendations.csv
│   ├── popular_movies.csv
│   ├── movies.csv
│   ├── users.csv
│   └── ratings.csv
└── screenshots/
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run Application.py
```

The Streamlit dashboard does not import LightFM at runtime because it reads the precomputed recommendation outputs generated during training.

---

## 📊 Dashboard Pages

- Home
- Personalized Recommendations
- Popular Movies
- Dataset Analytics
- Model Performance
- About Project

---

## 📷 Screenshots

```text
screenshots/
├── home.png
├── personalized_recommendations.png
├── popular_movies.png
├── dataset_analytics.png
├── model_performance.png
└── about_project.png
```

---

## 🔮 Future Enhancements

- Hybrid recommendations using movie genres
- Cold-start recommendations
- Similar-movie search
- Movie poster integration
- Live rating feedback
- Diversity-aware recommendation ranking

---

## 👩‍💻 Developed By

**Aruna V S**

Machine Learning | Data Science | Artificial Intelligence

