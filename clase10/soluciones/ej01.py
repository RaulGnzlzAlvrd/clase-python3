def nested_sum(t):
    acumulador = 0
    for element in t:
        acumulador += sum(element)
    return acumulador

assert nested_sum([]) == 0
assert nested_sum([[1], [2], [3]]) == 6
assert nested_sum([[1, 2], [3], [4, 5, 6]]) == 21
