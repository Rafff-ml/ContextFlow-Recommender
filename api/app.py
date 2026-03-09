from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import random
import requests
from dotenv import load_dotenv

from utils.data_loader import load_data
from utils.logger import setup_logger
from utils.exceptions import handle_exception

from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from models.ranking_model import train_ranking_model

from engine.user_profile import build_user_profile
from engine.feature_builder import build_features
from engine.candidate_generator import generate_candidates
from engine.ranker import rank_movies
from engine.trending_engine import get_trending_movies


# Load environment variables
load_dotenv()
TMDB_KEY = os.getenv("TMDB_API_KEY")

logger = setup_logger()

app = FastAPI()


# Enable CORS for UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------- INITIALIZATION --------

try:
    logger.info("Loading dataset")

    users, movies, ratings = load_data()

    matrix = build_user_item_matrix(ratings)
    similarity = compute_user_similarity(matrix)
    profiles = build_user_profile(ratings, movies)

    logger.info("Preparing ranking model")

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

    logger.info("Model trained successfully")

except Exception as e:
    logger.error(f"Initialization failed: {e}")


# -------- RECOMMENDATION ENDPOINT --------

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    try:
        logger.info(f"Recommendation requested for user {user_id}")

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

        logger.info("Recommendation generated")

        return {
            "recommended": recommended,
            "trending": trending,
            "discover": discover
        }

    except Exception as e:
        logger.error(f"Recommendation failed: {e}")
        return handle_exception(e)


# -------- POSTER ENDPOINT --------

@app.get("/poster/{movie}")
def get_poster(movie: str):

    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_KEY}&query={movie}"

        res = requests.get(url).json()

        if res["results"]:
            poster = res["results"][0]["poster_path"]

            return {
                "poster": f"https://image.tmdb.org/t/p/w500{poster}"
            }

        return {"poster": None}

    except Exception as e:
        logger.error(f"Poster fetch failed: {e}")
        return handle_exception(e)