import dbm
import pickle

from anagram_sets import signature, all_anagrams

def store_anagrams(file_name, dict_anagrams):
    db = dbm.open(file_name, 'c')
    for key, anagrams in dict_anagrams.items():
        db[pickle.dumps(key)] = pickle.dumps(anagrams)
    db.close()

def read_anagrams(file_name, word):
    db = dbm.open(file_name, 'c')
    key = signature(word)
    try:
        anagrams = pickle.loads(db[pickle.dumps(key)])
    except KeyError:
        anagrams = []
    db.close()
    return anagrams

def prompt_anagrams(db_name, prompt=">>>"):
    while True:
        print("¿Qué palabra deseas consultar? (exit para salir)")
        word = input(prompt + " ")
        if word == "exit()":
            break
        print(read_anagrams(db_name, word))

def main():
    db_name = "anagrams.db"
    words = "../../words.txt"
    anagrams = all_anagrams(words)
    store_anagrams(db_name, anagrams)
    prompt_anagrams(db_name)

if __name__ == "__main__":
    main()
