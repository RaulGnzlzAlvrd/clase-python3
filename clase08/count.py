def count(letter, word):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count
