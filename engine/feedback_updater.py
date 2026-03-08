def update_preferences(user_item_matrix, user_id, movie_id, feedback):

    user_index = user_id - 1
    
    if feedback == "like":
        user_item_matrix.iloc[user_index, movie_id-1] += 1

    elif feedback == "dislike":
        user_item_matrix.iloc[user_index, movie_id-1] -= 1 

    elif feedback == "skip":
        user_item_matrix.iloc[user_index, movie_id-1] -= 0.5


    return user_item_matrix          