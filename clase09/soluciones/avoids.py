def avoids(word, forbiden):
    '''
    Decide si la palabra word no usa ninguno de los caracteres
    en chars.

    word: String
    chars: String
    return: boolean
    '''
    for letter in word:
        if letter in forbiden:
            return False
    return True

caracteres = input("Ingresa los caracteres a omitir:\n")
file_name = "../words.txt"
fin = open(file_name)
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, caracteres):
        count += 1
print(count)
