def uses_all(word, required):
    '''
    Comprueba que word use al menos una vez cada caracter en chars

    word: String
    chars: String
    return: boolean
    '''
    return uses_only(required, word)

caracteres = input("Ingresa los caracteres deseados:\n")
print("-" * 10)
file_name = "../words.txt"
fin = open(file_name)
count = 0
for line in fin:
    word = line.strip()
    if uses_all(word, caracteres):
        print(word)
        count += 1
print(count)
