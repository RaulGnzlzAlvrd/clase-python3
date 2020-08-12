from ej02 import invert_dict

def histogram(word):
    d = dict()
    for c in word:
        d[c] = d.get(c, 0) + 1
        """
        if c not in d:
            d[c] = 0
        else:
            d[c] += 1
        """
    return d

def print_hist(hist):
    for k in sorted(hist):
        print(k, hist[k])

word = "parrot"
h = histogram(word)
print_hist(h)
print_hist(invert_dict(h))
