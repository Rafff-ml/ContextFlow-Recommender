def rank_movies(user_id, movie_ids, model):

    scores = []

    for movie in movie_ids:

        pred = model.predict([[user_id, movie]])[0]


        scores.append((movie, pred))

    scores.sort(key=lambda x: x[1], reverse=True) 


    return scores   