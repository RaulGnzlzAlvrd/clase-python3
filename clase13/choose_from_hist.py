import random
from histograma import histograma
from bisect import bisect_left

def choose_from_hist_v1(hist):
    elems = []
    for key, value in hist.items():
        elems.extend([key] * value)
    return random.choice(elems)


def choose_from_hist_v2(hist):
    keys = list(hist.keys())
    cum_list = cum_sum(list(hist.values()))
    n = sum(list(hist.values()))
    r = random.randint(1, n)
    index = bisect_left(cum_list, r)
    return keys[index]

def cum_sum(l):
    acc = 0
    res = []
    for e in l:
        acc += e
        res.append(acc)
    return res

t = ['a', 'b', 'a']
h = histograma(t)
cont = 0
for i in range(100):
    eleccion = choose_from_hist_v2(h)
    if 'a' == eleccion:
        cont += 1

print(cont)
