def middle(t):
    return t[1:-1]

assert middle([]) == []
assert middle([1]) == []
assert middle([1, 2]) == []
assert middle([1, 2, 3, 4]) == [2, 3]
assert middle([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 4, 5, 6]
