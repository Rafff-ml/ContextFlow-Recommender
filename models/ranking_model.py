from sklearn.ensemble import RandomForestRegressor

def train_ranking_model(features, labels):

    #X = ratings[["user_id","movie_id"]]
    #y = ratings["rating"]


    model = RandomForestRegressor(n_estimators=100)

    model.fit(features, labels)

    return model

