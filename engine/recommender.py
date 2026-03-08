import numpy as np 

def recommend_movies(user_id, user_item_matrix, similarity_matrix, top_n=5):

    user_index = user_id - 1

    user_similarity = similarity_matrix[user_index]

    weighted_ratings = np.dot(user_similarity, user_item_matrix.fillna(0))

    similarity_sum = np.sum(np.abs(user_similarity))

    scores = weighted_ratings / similarity_sum

    user_ratings = user_item_matrix.iloc[user_index]

    unseen_movies = user_ratings[user_ratings.isna()].index

    recommendations = []

    for movie in unseen_movies:
        recommendations.append((movie, scores[movie-1]))

    recommendations = sorted(
        recommendations,
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:top_n]