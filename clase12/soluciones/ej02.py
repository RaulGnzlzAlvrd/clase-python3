def file_to_list():
    file_name = "../../words.txt"
    fin = open(file_name)
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def build_anagrams(words):
    anagrams = dict()
    for word in words:
        key = tuple(sorted(word))
        anagrams.setdefault(key, [0]).append(word)
        anagrams[key][0] += 1
    return anagrams

def print_anagrams(d):
    for key in d:
        anagrams = d[key]
        if len(anagrams) > 2:
            print(anagrams[1:])

def print_anagrams_max_to_min(d):
    anagrams = sorted(d.values())[::-1]
    for anagram in anagrams:
        if anagram[0] < 2:
            break
        input()
        print(anagram)

def print_bingos(d):
    anagrams = sorted(d.values())[::-1]
    max = 0
    for anagram in anagrams:
        if len(anagram[1]) == 8 and len(anagram) >= max:
            print(tuple(sorted(anagram[1])))
            max = len(anagram)
        if len(anagram) < max:
            break

def start():
    anagrams = build_anagrams(file_to_list())
    ej = input("¿Qué ejercicio quieres probar? (1, 2, 3)\n")
    if ej == "1":
        print("Ej. 1:")
        print_anagrams(anagrams)
    elif ej == "2":
        print("Ej. 2:")
        print_anagrams_max_to_min(anagrams)
    elif ej == "3":
        print("Ej. 3:")
        print_bingos(anagrams)
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    start()
