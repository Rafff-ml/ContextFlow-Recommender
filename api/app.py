from utils.data_loader import load_data
from utils.logger import setup_logger

from models.preference_model import build_user_item_matrix
from models.similarity_model import compute_user_similarity
from models.ranking_model import train_ranking_model

from engine.candidate_generator import generate_candidates
from engine.ranker import rank_movies
from engine.user_profile import build_user_profile
from engine.feature_builder import build_features


logger = setup_logger()


try:

    logger.info("Loading dataset")

    users, movies, ratings = load_data()


    logger.info("Building user-item matrix")

    matrix = build_user_item_matrix(ratings)


    logger.info("Computing user similarity")

    similarity = compute_user_similarity(matrix)


    logger.info("Building user profiles")

    profiles = build_user_profile(ratings, movies)


    logger.info("Preparing training features")

    feature_rows = []
    labels = []

    for _, row in ratings.iterrows():

        f = build_features(
            row["user_id"],
            row["movie_id"],
            profiles,
            movies,
            matrix
        )

        feature_rows.append([
            f["genre_match"],
            f["popularity"]
        ])

        labels.append(row["rating"])


    logger.info("Training ranking model")

    model = train_ranking_model(feature_rows, labels)


    user_id = 1

    logger.info(f"Generating recommendations for user {user_id}")


    candidates = generate_candidates(
        user_id,
        matrix,
        similarity,
        movies,
        ratings
    )


    ranked_movies = rank_movies(
        user_id,
        candidates,
        model,
        profiles,
        movies,
        matrix
    )


    print("\nTop Recommended Movies\n")

    for movie_id, score in ranked_movies[:10]:

        title = movies[
            movies["movie_id"] == movie_id
        ]["title"].values[0]

        print(title, "->", round(score, 2))


    logger.info("Recommendation pipeline completed successfully")


except Exception as e:

    logger.error(f"Pipeline failed: {e}")

    print("Error occurred:", e)