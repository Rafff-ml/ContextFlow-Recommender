import pandas as pd


def load_data():

    # Ratings
    ratings = pd.read_csv(
        "data/u.data",
        sep="\t",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )


    # Movies with genre columns
    movies = pd.read_csv(
        "data/u.item",
        sep="|",
        encoding="latin-1",
        header=None
    )


    # Genre names from dataset
    genre_names = [
        "unknown","Action","Adventure","Animation","Children",
        "Comedy","Crime","Documentary","Drama","Fantasy",
        "Film-Noir","Horror","Musical","Mystery","Romance",
        "Sci-Fi","Thriller","War","Western"
    ]


    movies = movies[[0,1] + list(range(5,24))]
    movies.columns = ["movie_id","title"] + genre_names


    # Convert genre columns → genre string
    def combine_genres(row):

        g = []

        for genre in genre_names:
            if row[genre] == 1:
                g.append(genre)

        return "|".join(g)


    movies["genres"] = movies.apply(combine_genres, axis=1)

    movies = movies[["movie_id","title","genres"]]


    # Users
    users = pd.read_csv(
        "data/u.user",
        sep="|",
        names=["user_id","age","gender","occupation","zip"]
    )


    return users, movies, ratings