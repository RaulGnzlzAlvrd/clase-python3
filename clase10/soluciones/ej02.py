def cumsum(t):
    res = []
    acc = 0
    for elem in t:
        acc += elem
        res.append(acc)
    return res

assert cumsum([1, 2, 3]) == [1, 3, 6]
assert cumsum([1]) == [1]
assert cumsum([]) == []
