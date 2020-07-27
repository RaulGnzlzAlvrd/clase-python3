def alphabetical(word1, word2):
    if word1.upper() < word2.upper():
        return word1
    else:
        return word2

print(alphabetical("Piña", "banana"))
