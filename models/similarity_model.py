from sklearn.metrics.pairwise import cosine_similarity

def compute_user_similarity(user_item_matrix):

    similarity = cosine_similarity(
        user_item_matrix.fillna(0)
    )

    return similarity