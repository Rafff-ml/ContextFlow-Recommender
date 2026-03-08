def apply_context(recommendations, context):

    filtered = []

    for movie, score in recommendations:

        if context == "night":
            score = score * 1.1

        elif context == "weekend":
            score = score * 1.05


        filtered.append((movie, score))


    filtered.sort(key=lambda x: x[1], reverse=True)

    return filtered            