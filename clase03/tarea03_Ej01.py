def right_justify(s):
    print('-' * 70)
    spaces = ' ' * (70 - len(s))
    print(spaces + s)

right_justify("Hola como estás?")
