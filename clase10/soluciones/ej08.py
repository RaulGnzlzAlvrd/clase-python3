from random import randint

def generate_sample(size):
    res = []
    for i in range(size):
        res.append(generate_bithdate())
    return res

def generate_bithdate():
    month = randint(1, 12)
    first = 1
    last = 31
    if month == 2:
        last = 29
    if month not in [1, 3, 5, 7, 8, 10, 12]:
        last = 30
    day = randint(first, last)
    return [month, day]

def has_duplicates(t):
    if len(t) <= 1:
        return False
    else:
        return t[0] in t[1:] or has_duplicates(t[1:])

count = 0
samples = 10000
sample_size = 23
for i in range(samples):
    if has_duplicates(generate_sample(sample_size)):
        count += 1
print(100 / samples * count)
