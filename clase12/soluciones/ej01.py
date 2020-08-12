def histograma(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse

def most_frequent(s):
    freq = invert_dict(histograma(s))
    for i in sorted(freq)[::-1]:
        print(i, freq[i])

if __name__ == "__main__":
    text = "hola mundo, quiero saber como te encuentras el dia de hoy"
    most_frequent(text)
