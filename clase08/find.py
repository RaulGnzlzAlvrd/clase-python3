def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
