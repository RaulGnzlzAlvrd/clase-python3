from ej01 import file_to_list
from ej02 import in_bisect

def reverse_pairs(words):
    """
    Encuentra todos los pares reversibles de la lista words
    y regresa una lista con todos los pares.
    No considera palíndromos.

    words: listof String
    return: listof (list String String)
    """
    res = []
    for i in range(len(words)):
        word = words[i]
        reverse = word[::-1]
        if in_bisect(words[i+1:], reverse):
            res.append([word, reverse])
    return res

file_name = "../../../clase09/words.txt"
words = file_to_list(file_name)
print(reverse_pairs(words))
