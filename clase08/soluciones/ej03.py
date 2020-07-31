# 1.
def any_lowercase1(s):
    '''
    Nos dice si la primera letra de un string s es
    minúscula.

    s: String
    '''
    for c in s:
        if c.islower():
            return True
        else:
            return False

#2
def any_lowercase2(s):
    '''
    Siempre regresa la cadena "True" si s no es vacía.

    s: String
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#3
def any_lowercase3(s):
    '''
    Nos dice si la última letra de un string s
    es minúscula.

    s: String
    '''
    for c in s:
        flag = c.islower()
    return flag

#4
def any_lowercase4(s):
    '''
    Nos dice si el string s contiene una letra
    minúscula.

    s: String
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#5
def any_lowercase5(s):
    '''
    Nos dice si el string s tiene todas sus letras
    minúsculas.

    s: String
    '''
    for c in s:
        if not c.islower():
            return False
    return True
