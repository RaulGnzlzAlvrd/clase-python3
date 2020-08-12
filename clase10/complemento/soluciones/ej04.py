from ej01 import file_to_list
from ej02 import in_bisect
from time import time

def search_interlock(word, words):
    word1 = word[::2]
    word2 = word[1::2]
    if in_bisect(words, word1) and in_bisect(words, word2):
        print(word1, word2, word)

def take_time(f):
    start = time()
    f()
    end = time()
    elapsed = end - start
    print("Time in seconds:", elapsed)

def foo():
    file_name = "../../../clase09/words.txt"
    words = file_to_list(file_name)
    for word in words:
        search_interlock(word, words)

take_time(foo);
