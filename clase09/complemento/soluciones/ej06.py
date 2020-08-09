def has_three(word):
    '''
    Comprueba que word contenga tres pares consecutivos de dobles letras.
    Ej: "Caammiiseta"

    word: String
    return: boolean
    '''
    # Palabras menores a 6 no tienen los 3 pares
    if len(word) < 6:
        return False
    # LLeva el conteo de los pares consecutivos
    count = 0
    index = 0
    while index < len(word):
        # Usamos last para comparar con el caracter actual
        last = ""
        if index != 0:
            last = word[index-1]
        if word[index] == last:
            count += 1
            # Al tener 3 consecutivos terminamos
            if count == 3:
                return True
            # Saltamos dos espacios para comprobar el siguiente par
            index += 2
        else:
            # Reiniciamos el contador
            count = 0
            index += 1
    return False

# Pruebas unitarias de has_three
assert has_three("aabbcc")
assert not has_three("abc")
assert not has_three("aabbcbcab")
assert not has_three("mississippi")
assert has_three("missssppi")
assert not has_three("holamiss")

# Buscamos las palabras que tienen 3 pares de letras consecutivos
fin = open("../words.txt")
count = 0
for line in fin:
    word = line.strip()
    if has_three(word):
        print(word)
        count += 1
print("Total: %i" % (count))
