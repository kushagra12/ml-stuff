from math import sqrt

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0,
                     'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0,
                      'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


def sim_distance(p1, p2, prefs):
    sim = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            sim[item] = 1

    # If they don't have any similar movies
    if len(sim) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in sim])

    return 1 / (1 + sum_of_squares)


def sim_pearson(p1, p2, prefs):
    sim = []

    for item in prefs[p1]:
        if item in prefs[p2]:
            sim.append(item)

    n = len(sim)
    if n == 0:
        return 0

    sum1 = sum([prefs[p1][item] for item in sim])
    sum2 = sum([prefs[p2][item] for item in sim])

    sum_sq1 = sum([pow(prefs[p1][item], 2) for item in sim])
    sum_sq2 = sum([pow(prefs[p2][item], 2) for item in sim])

    p_sum = sum([prefs[p1][item] * prefs[p2][item] for item in sim])

    num = p_sum - (sum1 * sum2) / n
    den = sqrt((sum_sq1 - pow(sum1, 2) / n) * (sum_sq2 - pow(sum2, 2) / n))

    if den == 0:
        return 0

    return num / den


def flip_params(prefs):
    result = {}

    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]

    return result


def top_matches(person, pref, similarity=sim_pearson, n=5):
    similarity_points = []

    for critic in pref:
        if person != critic:
            similarity_points.append(
                {
                    'similarity': similarity(person, critic, pref),
                    'name': critic,
                }
            )

    similarity_points = sorted(similarity_points, key=lambda k: k['similarity'], reverse=True)

    return similarity_points[0:n]


def get_recommendations(person, prefs, similarity=sim_pearson):
    totals = {}
    sum_similar = {}

    for other in prefs:
        if other == person: continue

        sim = similarity(person, other, prefs)

        if sim < 0: continue

        for item in prefs[other]:
            if item not in prefs[person]:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                sum_similar.setdefault(item, 0)
                sum_similar[item] += sim

    recommendations = [(total / sum_similar[item], item) for item, total in totals.items()]

    recommendations.sort()
    recommendations.reverse()

    return recommendations
