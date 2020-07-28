# Imprime todas las líneas formateadas del archivo file_name
file_name = "words.txt"
fin = open(file_name)
for line in fin:
    word = line.strip()
    print(word)
