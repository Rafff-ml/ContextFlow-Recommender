from utils.data_loader import load_data
from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from engine.recommender import recommend_movies
from engine.context_filter import apply_context

from models.content_model import build_content_similarity
from engine.content_recommender import recommend_similar_movies

from models.ranking_model import train_ranking_model
from engine.ranker import rank_movies


# Load dataset
users, movies, ratings = load_data()

# Build collaborative filtering components
matrix = build_user_item_matrix(ratings)
similarity = compute_user_similarity(matrix)

# Get recommendations for user 1
recs = recommend_movies(1, matrix, similarity)

# Apply context
context_recs = apply_context(recs, "night")

print("\nRecommended Movies:\n")

for movie_id, score in context_recs:
    title = movies[movies["movie_id"] == movie_id]["title"].values[0]
    print(title, score)


# -------- Content Based Section -------- #

content_similarity = build_content_similarity(movies)

print("\nMovies similar to Toy Story:\n")

toy_story_id = movies[movies["title"].str.contains("Toy Story")]["movie_id"].values[0]

similar_movies = recommend_similar_movies(
    toy_story_id,
    movies,
    content_similarity
)

print(similar_movies["title"])


#------------- add ranking step ------------- #

model = train_ranking_model(ratings)

candidate_movies = matrix.columns[:50]

ranked = rank_movies(1, candidate_movies, model)

print("\nTop Ranked movies\n")

for movie_id, score in ranked[:5]:
    title = movies[movies["movie_id"]==movie_id]["title"].values[0]

    print(title, score)