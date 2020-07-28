def has_no_e(word):
    '''
    Verifica si word no contiene la letra 'e'

    word: String
    '''
    for char in word:
        if char == 'e':
            return False
    return True


file_name = "words.txt"
fin = open(file_name)
total = 0
no_e = 0
for line in fin:
    total += 1
    word = line.strip()
    if has_no_e(word):
        no_e += 1
        print(word)

porcentaje = 100 / total * no_e
print("%.2f" % (porcentaje))
