def has_duplicates(t):
    if len(t) <= 1:
        return False
    else:
        return t[0] in t[1:] or has_duplicates(t[1:])

assert not has_duplicates([])
assert not has_duplicates([1])
assert not has_duplicates([1, 2])
assert has_duplicates([1, 1])
assert has_duplicates([1, 2, 3, 4, 5, 6, 6])
assert has_duplicates([1, 2, 3, 4, 5, 6, 1])
assert not has_duplicates([1, 2, 3, 4, 5, 6, 7])
