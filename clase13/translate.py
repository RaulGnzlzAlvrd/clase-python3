import string

def get_table():
    table = dict()
    for c in string.punctuation:
        table[ord(c)] = ord(' ')
    return table

s = "¿Cómo has estado, amigo?\nEspero que bien."
s.translate(get_table())
