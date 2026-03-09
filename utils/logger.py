import logger

def setup_layer():

    logger = logging.getLogger("contextflow")

    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("app.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )


    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger