import random

def choose_from_hist(h):
    size = sum(h.values())
    while True:
        candidate = random.choice(list(h))
        if random.random() < h[candidate] / size:
            return candidate

h = {'a': 2, 'b': 1}
res = {'a': 0, 'b': 0}
for i in range(1000):
    choosen = choose_from_hist(h)
    res[choosen] += 1

def calcula_porcentaje(d):
    size = sum(d.values())
    res = dict()
    for k in d:
        res[k] = d[k] / size * 100
    return res

print(calcula_porcentaje(res))
