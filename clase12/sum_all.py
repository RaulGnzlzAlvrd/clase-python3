def sum_all(*args):
    return sum(args)

assert sum_all(1, 2, 3) == 6
assert sum_all(3) == 3
assert sum_all() == 0
assert sum_all(3, 3, 4, 7, 1) == 18

l = [1, 2, 3]
assert sum_all(*l) == 6

t = 1, 2, 3
assert sum_all(*t) == 6
