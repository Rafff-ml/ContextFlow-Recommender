from engine.feature_builder import build_features


def rank_movies(user_id, candidates, model, profiles, movies, user_item_matrix):

    scored = []

    for movie in candidates:

        f = build_features(user_id, movie, profiles, movies, user_item_matrix)


        feature_vector = [[
            f["genre_match"],
            f["popularity"]
        ]]


        score = model.predict(feature_vector)[0]


        scored.append((movie, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored    