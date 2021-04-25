#!/bin/python3

ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N', 'Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number_code = dict([(a,i) for i,a in enumerate(ABC)])

def translate_char(c, t):
    try:
        low = c.islower()
        if low:
            c = c.upper()
        code = (number_code[c] + t) % 27
        result = ABC[code]
        if low:
            result = result.lower()
        return result
    except:
        return c

def encode(clear, key):
    return translate(clear, key)
    
def decode(clear, key):
    return translate(clear, -key)

def translate(text, key):
    translated = ""
    for x in text:
        translated += translate_char(x, key)
    return translated

cadena = "¿Cuando puedo ir a tu casa, Pau?"
key = 2

encoded = encode(cadena, key)
decoded = decode(encoded, key)

print(encoded, decoded)
