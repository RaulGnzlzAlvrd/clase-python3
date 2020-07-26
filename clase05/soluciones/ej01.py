def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("¡Madre mía, Fermat estaba equivocado!")
    else:
        print("No, no funciona...")

def int_input(mensaje):
    raw = input(mensaje + "\n")
    return int(raw)

def input_fermat():
    a = int_input("Ingresa el valor de a:")
    b = int_input("Ingresa el valor de b:")
    c = int_input("Ingresa el valor de c:")
    n = int_input("Ingresa el valor de n:")
    check_fermat(a, b, c, n)

input_fermat()
