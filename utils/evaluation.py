import numpy as np 

def precision_at_k(recommended, relevant, k=10):

    recommended_k = recommended[:k]

    hits = len(set(recommended_k) & set(relevant))

    return hits / k 


def recall_at_k(recommended, relevant, k=10):

    recommended_k = recommended[:k]

    hits = len(set(recommended_k) & set(relevant))

    return hits / len(relevant) if relevant else 0 


def rmse(y_true, y_pred):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    return np.sqrt(np.mean((y_true - y_pred) ** 2))