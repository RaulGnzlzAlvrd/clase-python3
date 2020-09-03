import string

####### str.translate()
def get_table():
    table = dict()
    for c in string.punctuation + '¿':
        table[ord(c)] = ord(' ')
    return table

s = "¿Cómo has estado, amigo?\nEspero que bien."
a = s.translate(get_table())
print(a)

################### str.strip()
b = s.split()
c = []
for w in b:
    c.append(w.strip(string.punctuation + '¿'))
b = " ".join(c)
print(b)

############### str.replace()
a = s
for p in string.punctuation + '¿':
    a = a.replace(p, ' ')
print(a)
