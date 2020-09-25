def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('ejemplo.py'))
    s = '1 2 \t 3 \n 4'
    print(s)
    print(repr(s))
