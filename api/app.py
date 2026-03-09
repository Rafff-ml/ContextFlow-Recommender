from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.data_loader import load_data
from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from models.ranking_model import train_ranking_model

from engine.candidate_generator import generate_candidates
from engine.ranker import rank_movies
from engine.user_profile import build_user_profile
from engine.feature_builder import build_features
from engine.trending_engine import get_trending_movies

import random


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


users, movies, ratings = load_data()

matrix = build_user_item_matrix(ratings)

similarity = compute_user_similarity(matrix)

profiles = build_user_profile(ratings, movies)


# Train ranking model
feature_rows = []
labels = []

for _, row in ratings.iterrows():

    f = build_features(
        row["user_id"],
        row["movie_id"],
        profiles,
        movies,
        matrix
    )

    feature_rows.append([
        f["genre_match"],
        f["popularity"]
    ])

    labels.append(row["rating"])

model = train_ranking_model(feature_rows, labels)


@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    candidates = generate_candidates(
        user_id,
        matrix,
        similarity,
        movies,
        ratings
    )

    ranked = rank_movies(
        user_id,
        candidates,
        model,
        profiles,
        movies,
        matrix
    )

    recommended = []

    for movie_id, score in ranked[:20]:

        title = movies[movies["movie_id"] == movie_id]["title"].values[0]

        recommended.append(title)


    trending_ids = get_trending_movies(ratings, 20)

    trending = movies[
        movies["movie_id"].isin(trending_ids)
    ]["title"].tolist()


    discover = random.sample(
        movies["title"].tolist(),
        20
    )


    return {
        "recommended": recommended,
        "trending": trending,
        "discover": discover
    }