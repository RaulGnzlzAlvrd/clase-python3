def saludos(nombre):
    print("¡Buenas tardes!")
    print("Bienvenid@ a nuestro equipo, " + nombre + "!")

def input_saludos():
    nombre = input("Ingresa tu nombre:\n")
    saludos(nombre)

input_saludos()
