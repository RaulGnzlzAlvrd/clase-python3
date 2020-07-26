def is_reverse(word1, word2):
    '''
    Revisa si dos palabras son la misma palabra pero en reversa.

    word1: String
    word2: String
    '''
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1
    while j >= 0:
        print(str(i) + " " + str(j))
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_reverse("oso", "oso"))
