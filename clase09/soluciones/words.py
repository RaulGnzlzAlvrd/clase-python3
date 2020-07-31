def print_all(file_name):
    '''
    Imprime todas las línas del archivo file_name

    file_name: String
    '''
    fin = open(file_name)
    for line in fin:
        # Quita el salto de línea
        word = line.strip()
        print(word)

file_name = "words.txt"
print_all(file_name)
