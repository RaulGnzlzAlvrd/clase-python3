def file2list(file):
    return

def foo(file, size=2):
    book = file2list(file)
    # ["En", "un", "lugar", "lejano", "del", "viejo", "oeste"]
    prefix = tuple(book[:size]) # ["En", "un", "lugar", "lejano"]
    # ("En", "un", "lugar", "lejano")
    d = dict()
    for word in book[size:]:
        sufijos = d.setdefault(prefix, dict())
        sufijos[word] = 1
        prefix = prefix[1:] + (word,)
    return d
