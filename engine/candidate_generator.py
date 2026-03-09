from engine.exploration_controller import mix_recommendations
from engine.trending_engine import get_trending_movies
import random

def generate_candidates(user_id, user_item_matrix, similarity_matrix, movies, ratings):

    user_index = user_id - 1

    # Collaborative Filtering
    user_similarity = similarity_matrix[user_index]

    similar_users = user_similarity.argsort()[-10:]

    personalized = []

    for u in similar_users:
        watched = user_item_matrix.iloc[u].dropna().index.tolist()
        personalized.extend(watched)

    personalized = list(set(personalized))


    #TRending candidates (most rated movies) 
    trending = get_trending_movies(ratings, 200)

    #Discovery candidates
    discovery = random.sample(list(movies["movie_id"]), 100)


    candidates = mix_recommendations(personalized, trending, discovery)

    return list(set(candidates))   