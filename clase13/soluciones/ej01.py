import string

def get_table():
    res = dict()
    characters = "“―‘”" + string.punctuation + string.digits
    for p in characters:
        key = ord(p)
        res[key] = res.get(key, ' ')
    return res

def read_file(file_name):
    fin = open(file_name)
    res = dict()
    total = 0
    start_header = "START OF THIS PROJECT GUTENBERG EBOOK"
    end_header = "END OF THIS PROJECT GUTENBERG EBOOK"
    for line in fin:
        if start_header in line:
            break

    for line in fin:
        if end_header in line:
            break
        words = line.translate(get_table()).split()
        for word in words:
            total += 1
            lower = word.lower()
            res[lower] = res.get(lower, 0) + 1
    return res, total, len(res)

def print_sumary(t):
    d = t[0]
    for w in d:
        print(w, "\b:", d[w])
    print("*" * 15)
    print("Total words:", t[1])
    print("Different words:", t[2])

def invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse

def print_most_frequent(d, n):
    freq = invert_dict(d)
    count = 0
    for i in sorted(freq)[::-1]:
        for word in freq[i]:
            if count > n:
                break
            count += 1
            print(word, i)

def file2dict():
    file = "../../words.txt"
    fin = open(file)
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = 0
    return d

def in_dict(d, v):
    return v in d

def print_not_in_list(d, words):
    count = 0
    for w in d:
        if w not in words:
            print(w)
            count += 1
    print(count)

names = ["julio", "animals", "mosqueteros"]
extension = ".txt"
directory = "./files/"
for name in names:
    print("*" * 20)
    path = directory + name + extension
    data = read_file(path)
    # print(name, "\b:", data[2])
    # print_most_frequent(data[0], 20)
    print_not_in_list(data[0], file2dict())
