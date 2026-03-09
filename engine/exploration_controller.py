import random

def mix_recommendations(personalized, trending, discovery, total=100):

    p_count = int(total * 0.7)
    t_count = int(total * 0.2)
    d_count = int(total * 0.1)


    p = personalized[:p_count]
    t = trending[:t_count]
    d = discovery[:d_count]

    combined = p + t + d

    random.shuffle(combined)

    return combined