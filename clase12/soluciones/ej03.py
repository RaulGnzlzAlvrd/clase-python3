from ej02 import file_to_list, build_anagrams

def is_metathesis_pair(w1, w2):
    diff = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff += 1
    return diff == 2

def print_metathesis_pair(d):
    for key in d:
        anagrams = d[key][1:]
        for i in range(len(anagrams)):
            for j in range(i, len(anagrams)):
                word1 = anagrams[i]
                word2 = anagrams[j]
                if is_metathesis_pair(word1, word2):
                    print(word1, word2)

if __name__ == "__main__":
    print_metathesis_pair(build_anagrams(file_to_list()))
