def int_input(mensaje):
    raw = input(mensaje + "\n")
    return int(raw)

def is_triangle(a, b, c):
    if a >= b and a >= c and a > b + c:
        print("No")
    elif b >= a and b >= c and b > a + c:
        print("No")
    elif c >= b and c >= a and c > b + a:
        print("No")
    else:
        print("Sí")

def input_triangle():
    a = int_input("Ingresa el valor de a:")
    b = int_input("Ingresa el valor de b:")
    c = int_input("Ingresa el valor de c:")
    is_triangle(a, b, c)

input_triangle()
