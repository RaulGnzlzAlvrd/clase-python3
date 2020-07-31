def rotate_letter(letter, displacement):
    '''
    Regresa la letra resultante de rotar letter
    una cantidad displacement de esplacios.

    letter: Char
    displacement: Int

    return: Char
    '''
    # La letra 'A' tiene indice 65 y la 'a' 97
    base = 65
    if letter.islower():
        base = 97
    # Obtenemos el código de la letra suponiendo que 'A' y 'a' son 0
    original = ord(letter) - base
    # Obtenemos el código rotado
    new = (original + displacement) % 26
    # Obtenemos el indice desplazandolo a la base
    return chr(new + base)

def rotate_word(word, displacement):
    new = ""
    for letter in word:
        new = new + rotate_letter(letter, displacement)
    return new

print(rotate_word("melon", -10))
