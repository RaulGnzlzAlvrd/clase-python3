def file2dict():
    file = "../../clase09/words.txt"
    fin = open(file)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 0
    return d

def in_dict(d, v):
    return v in d
