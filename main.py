from utils.data_loader import load_data

from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from models.ranking_model import train_ranking_model

from engine.candidate_generator import generate_candidates
from engine.ranker import rank_movies
from engine.user_profile import build_user_profile


# Load dataset
users, movies, ratings = load_data()


# Build user-item matrix
matrix = build_user_item_matrix(ratings)


# Compute user similarity
similarity = compute_user_similarity(matrix)


# Train ranking model
model = train_ranking_model(ratings)


# Build user profiles
profiles = build_user_profile(ratings, movies)


# Select user
user_id = 1


# Show example profile
print("\nUser Profile\n")
print(profiles[user_id])


# Generate candidate movies
candidates = generate_candidates(user_id, matrix, similarity, movies)


# Rank candidates
ranked_movies = rank_movies(user_id, candidates, model)


print("\nTop Recommended Movies\n")


# Print top recommendations
for movie_id, score in ranked_movies[:10]:

    title = movies[movies["movie_id"] == movie_id]["title"].values[0]

    print(title, "->", round(score, 2))
    