def chop(t):
    if len(t) > 0:
        del t[0]
    if len(t) > 0:
        del t[-1]

a = []
chop(a)
assert a == []

b = [1]
chop(b)
assert b == []

c = [1, 2]
chop(c)
assert c == []

d = [1, 2, 3, 4]
chop(d)
assert d == [2, 3]

e = [1, 2, 3, 4, 5, 6, 7]
chop(e)
assert e == [2, 3, 4, 5, 6]
