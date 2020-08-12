def is_sorted(t):
    tmp = t[:]
    tmp.sort()
    return tmp == t

assert is_sorted([1, 2, 2])
assert not is_sorted(['b', 'a'])
assert is_sorted([])
