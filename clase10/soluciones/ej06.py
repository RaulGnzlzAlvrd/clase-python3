def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    return list1 == list2

assert is_anagram("abcd", "cdab")
assert is_anagram("", "")
assert is_anagram("hola mundo", "hundo mola")
