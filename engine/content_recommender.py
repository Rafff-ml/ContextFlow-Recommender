def recommend_similar_movies(movie_id, movies, similarity_matrix, top_n=5):

    idx = movies[movies["movie_id"] == movie_id].index[0]

    scores = list(enumerate(similarity_matrix[idx]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    scores = scores[1:top_n+1]

    movie_indices = [i[0] for i in scores]

    return movies.iloc[movie_indices]


    