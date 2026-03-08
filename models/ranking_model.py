from sklearn.ensemble import RandomForestRegressor

def train_ranking_model(ratings):

    X = ratings[["user_id","movie_id"]]
    y = ratings["rating"]


    model = RandomForestRegressor(n_estimators=50)

    model.fit(X,y)

    return model

