import random

def generate_candidates(user_id, user_item_matrix, similarity_matrix, movies):

    user_index = user_id - 1

    # Collaborative Filtering
    user_similarity = similarity_matrix[user_index]

    similar_users = user_similarity.argsort()[-10:]

    Collaborative_candidates = []

    for u in similar_users:
        watched = user_item_matrix.iloc[u].dropna().index.tolist()
        Collaborative_candidates.extend(watched)

    Collaborative_candidates = list(set(Collaborative_candidates))


    #TRending candidates (most rated movies) 
    trending = user_item_matrix.count().sort_values(ascending=False).head(100).index.tolist()

    #Discovery candidates
    discovery = random.sample(list(movies["movie_id"]), 50)


    candidates = list(set(Collaborative_candidates + trending + discovery))

    return candidates   