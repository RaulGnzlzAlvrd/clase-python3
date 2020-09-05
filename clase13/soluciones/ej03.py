from random import choice, randint
from bisect import bisect

def markov_analysis(file_path, length=2, mapping=dict()):
    fin = open(file_path)
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

def choice_key(d):
    return choice(list(d.keys()))

def make_sentence(mapping, length=50):
    prefix = choice_key(mapping)
    sentence = " ".join(list(prefix))
    for i in range(length):
        if prefix not in mapping:
            prefix = choice_key(mapping)
        word = choice_key(mapping[prefix])
        sentence += " " + word
        prefix = shift(prefix, word)
    return sentence

def print_dict(d):
    for k, v in d.items():
        print(k, v, sep=": ")

def main():
    files = ["quijote", "noches", "venezuela1"]
    mapping = dict()
    for file in files:
        path = "files/%s.txt" % file
        markov_analysis(path, 3, mapping)
    print(make_sentence(mapping, 50))

if __name__ == "__main__":
    main()
