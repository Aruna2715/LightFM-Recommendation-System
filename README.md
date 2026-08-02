# 🎬 MovieMatch AI

## Personalized Movie Recommendation System using LightFM

![Python](https://img.shields.io/badge/Python-3.13-f5c518?logo=python)
![LightFM](https://img.shields.io/badge/Model-LightFM-e50914)
![Dataset](https://img.shields.io/badge/Dataset-MovieLens%20100K-ff8a00)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b?logo=streamlit)

---

## 📌 Project Overview

MovieMatch AI is a personalized movie discovery platform built with **LightFM** and the **MovieLens 100K** dataset.

The project converts ratings of 4 and 5 into positive user-item interactions, trains a LightFM model with **WARP loss**, evaluates ranking performance, and generates top-N movie recommendations.

The Streamlit dashboard presents the project through a cinematic interface inspired by modern streaming platforms.

---

## ✨ Features

- Personalized top-N movie recommendations
- Viewer profile display
- Movie recommendation cards
- IMDb links
- Trending and highly rated movie leaderboards
- Rating and audience analytics
- Gauge-based model evaluation
- Downloadable recommendation results
- Premium cinema-inspired interface

---

## 📂 Dataset

| Data | Count |
|---|---:|
| Users | 943 |
| Movies | 1,682 |
| Ratings | 100,000 |
| Positive Interactions | 55,375 |

Ratings of **4 and 5** were treated as positive interactions.

---

## 🧠 Final Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | LightFM |
| Loss | WARP |
| Latent Components | 50 |
| Learning Rate | 0.03 |
| Epochs | 40 |
| Threads | 1 |

---

## 📈 Final Results

| Metric | Score |
|---|---:|
| Train Precision@10 | **59.42%** |
| Test Precision@10 | **21.77%** |
| Test Recall@10 | **24.62%** |
| Test AUC | **93.99%** |

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

The deployed dashboard reads the precomputed recommendation outputs generated during model training.

---

## 📊 Dashboard Sections

- Discover
- For You
- Trending
- Audience Insights
- Model Studio
- About

---

## 📷 Suggested Screenshots

```text
screenshots/
├── discover.png
├── for_you.png
├── trending.png
├── audience_insights.png
├── model_studio.png
└── about.png
```

---

## 🔮 Future Enhancements

- Genre-aware hybrid recommendations
- Cold-start support
- Similar-movie search
- Poster and trailer integration
- Real-time rating feedback
- Diversity-aware ranking

---

## 👩‍💻 Developed By

**Aruna V S**

Machine Learning | Data Science | Artificial Intelligence



