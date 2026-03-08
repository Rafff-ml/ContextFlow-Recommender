# ContextFlow AI Recommender

Hybrid Movie Recommendation System built using machine learning and a modern web interface.

## Features

* Collaborative Filtering
* Content-Based Filtering
* Feedback Learning
* Context-Aware Recommendations
* ML Ranking Model
* FastAPI Backend
* Interactive Web UI

## Dataset

MovieLens 100K dataset from GroupLens Research.

## Tech Stack

Python
Pandas
Scikit-Learn
FastAPI
HTML / CSS / JavaScript

## System Architecture

Dataset → User Matrix → Similarity Engine → Ranking Model → FastAPI → Web UI

## Run Locally

Clone repository

```
git clone https://github.com/YOUR_USERNAME/contextflow-recommender.git
cd contextflow-recommender
```

Install dependencies

```
pip install -r requirements.txt
```

Run backend

```
uvicorn api.app:app --reload
```

Open UI

```
ui/index.html
```

## Future Improvements

* Multi-language movie support
* Deep learning recommendation model
* Real-time feedback learning
* Deployment
