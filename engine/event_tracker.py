import pandas as pd 
import os
from datetime import datetime

EVENT_FILE = "data/events.csv"


def log_event(user_id, movie_id, event_type):

    event = {
        "user_id": user_id,
        "movie_id": movie_id,
        "event_type": event_type,
        "tiemstamp": datetime.now()
    }

    df = pd.DataFrame([event])


    if os.path.exists(EVENT_FILE):
        df.to_csv(EVENT_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(EVENT_FILE, mode="w", header=True, index=False)

        
            