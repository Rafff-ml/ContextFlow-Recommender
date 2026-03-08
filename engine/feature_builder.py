def build_features(user_id, movie_id, profiles, movies, user_item_matrix):

    features = {}

    # user genre preference
    user_profile = profiles.get(user_id, {})

    movie_row = movies[movies["movie_id"] == movie_id]

    genres = movie_row["genres"].values[0].split("|")

    genre_score = 0

    for g in genres:
        genre_score += user_profile.get(g, 0)


    features["genre_match"] = genre_score 


    # movie popularity
    popularity = user_item_matrix[movie_id].count()

    features["popularity"] = popularity 


    return features  