import pandas as pd 

def build_user_profile(ratings, movies):

    data = ratings.merge(movies, on="movie_id")

    user_profiles = {}

    for user_id, group in data.groupby("user_id"):

        genre_scores = {}

        for _, row in group.iterrows():

            genres = str(row["genres"]).split("|")

            rating = row["rating"]

            for g in genres:

                genre_scores[g] = genre_scores.get(g, 0) + rating

        user_profiles[user_id] = genre_scores

    return user_profiles            