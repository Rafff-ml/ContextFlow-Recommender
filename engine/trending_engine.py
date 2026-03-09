import pandas as pd 

def get_trending_movies(ratings, top_n=50):

    rating_count = ratings.groupby("movie_id").size()

    avg_rating = ratings.groupby("movie_id")["rating"].mean()

    trending = pd.DataFrame({
        "rating_count": rating_count,
        "avg_rating": avg_rating
    })


    trending["score"] = trending["rating_count"] * trending["avg_rating"]

    trending = trending.sort_values("score", ascending=False)

    return trending.index.tolist()[:top_n]