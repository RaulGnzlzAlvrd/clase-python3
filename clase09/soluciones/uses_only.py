def uses_only(word, available):
    '''
    Comprueba que word use solamente letras en chars

    word: String
    chars: String
    return: boolean
    '''
    for letter in word:
        if not letter in available:
            return False
    return True

caracteres = input("Ingresa los caracteres deseados:\n")
file_name = "../words.txt"
fin = open(file_name)
for line in fin:
    word = line.strip()
    if uses_only(word, caracteres):
        print(word)
