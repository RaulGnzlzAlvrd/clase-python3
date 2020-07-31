def is_abecedarian(word):
    '''
    Comprueba si las letras en word están en orden alfabético

    word: String
    return: boolean
    '''
    index = 0
    while index < len(word) - 1:
        if word[index] > word[index + 1]:
            return False
        index += 1
    return True

file_name = "../words.txt"
fin = open(file_name)
abecedarian = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        abecedarian += 1

print(abecedarian)












def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
