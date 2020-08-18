from random import choice, randint
from bisect import bisect

def markov_analysis(file_path, length=2):
    fin = open(file_path)
    mapping = dict()
    prefix = init_prefix(length)
    for line in fin:
        words = line.split()
        for word in words:
            if None not in prefix:
                add_value(mapping, prefix, word)
            prefix = shift(prefix, word)
    return mapping

def init_prefix(n):
    return tuple([None] * n)

def shift(prefix, word):
    return prefix[1:] + (word,)

def add_value(d, k, v):
    freq = d.setdefault(k, dict())
    freq[v] = freq.get(v, 0) + 1

def cum_sum(l):
    cum = 0
    res = []
    for i in l:
        cum += i
        res.append(cum)
    return res

def choose_from_hist(h):
    words = list(h.keys())
    cum = cum_sum(h.values())
    total = sum(h.values())
    index = bisect(cum, randint(0, total-1))
    return words[index]

def make_sentence(mapping, length=50):
    prefix = choice(list(mapping.keys()))
    sentence = list(prefix)
    for i in range(length):
        if prefix not in mapping:
            break
        word = choose_from_hist(mapping[prefix])
        sentence.append(word)
        prefix = shift(prefix, word)
    return " ".join(sentence)

def print_dict(d):
    for k, v in d.items():
        print(k, v, sep=": ")

path = "files/quijote.txt"
mapping = markov_analysis(path, 3)
print(make_sentence(mapping, 500))
