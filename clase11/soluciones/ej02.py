def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        inverse.setdefault(val, []).append(k)
        """
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(key)
        """
    return inverse
