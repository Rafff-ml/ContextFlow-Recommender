from utils.data_loader import load_data

from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from models.ranking_model import train_ranking_model

from engine.candidate_generator import generate_candidates
from engine.ranker import rank_movies
from engine.user_profile import build_user_profile
from engine.feature_builder import build_features


# Load dataset
users, movies, ratings = load_data()


# Build user-item matrix
matrix = build_user_item_matrix(ratings)


# Compute similarity between users
similarity = compute_user_similarity(matrix)


# Build user preference profiles
profiles = build_user_profile(ratings, movies)


# Build training dataset for ranking model
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


# Train ML ranking model
model = train_ranking_model(feature_rows, labels)


# Select user
user_id = 1


print("\nUser Profile\n")
print(profiles[user_id])


# Generate candidate movies
candidates = generate_candidates(
    user_id,
    matrix,
    similarity,
    movies,
    ratings
)


# Rank candidates
ranked_movies = rank_movies(
    user_id,
    candidates,
    model,
    profiles,
    movies,
    matrix
)


print("\nTop Recommended Movies\n")


# Display top recommendations
for movie_id, score in ranked_movies[:10]:

    title = movies[movies["movie_id"] == movie_id]["title"].values[0]

    print(title, "->", round(score, 2))
    