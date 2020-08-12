def file_to_list(file_name):
    """
    Convierte cada linea del archivo con dirección file_name y
    los convierte en elementos de una lista, regresa esa lista.

    file_name: String
    return: list
    """
    fin = open(file_name)
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res
