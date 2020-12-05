def list_intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))


def list_difference(list_1, list_2):
    return list(set(list_1) - set(list_2))
