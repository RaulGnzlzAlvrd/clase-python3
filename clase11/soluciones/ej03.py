def has_duplicates(t):
    d = dict()
    for elem in t:
        if elem in d:
            return True
        d[elem] = 0
    return False
