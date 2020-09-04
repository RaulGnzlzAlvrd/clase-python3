import os

def sed(old, new, origin, destination):
    try:
        content = open(origin).read()
        fout = open(destination, 'w')
        fout.write(content.replace(old, new))
        fout.close()
    except:
        print("Algo salió mal! :(")

sed("ola\n", "hola ", "ola.txt", "hola.txt")
