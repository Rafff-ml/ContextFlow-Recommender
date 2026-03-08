import pandas as pd

def build_user_item_matrix(ratings):

    user_item_matrix = ratings.pivot_table(
        index="user_id",
        columns="movie_id",
        values="rating"
    )


    return user_item_matrix