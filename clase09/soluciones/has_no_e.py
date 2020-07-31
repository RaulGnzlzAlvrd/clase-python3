def has_no_e(word):
    '''
    Revisa si la palabra no usa la letra e

    word: String
    return: boolean
    '''
    for char in word:
        if char == 'e':
            return False
    return True


file_name = "../words.txt"
fin = open(file_name)
no_e = 0
total = 0

# Imprimimos las palabras que no tienen e y hacemos el conteo
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)
        no_e += 1
    total += 1

# Calculamos el porcentaje de las palabras que no tienen e
percentage = 100 / total * no_e
print("%.2f" % (percentage) + "%" )
