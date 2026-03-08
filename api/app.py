from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.data_loader import load_data
from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from engine.recommender import recommend_movies

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

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    recs = recommend_movies(user_id, matrix, similarity)

    results = []

    for movie_id, score in recs:
        title = movies[movies["movie_id"] == movie_id]["title"].values[0]
        results.append(title)

    return {"recommendations": results}