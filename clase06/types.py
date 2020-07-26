def factorial(n):
    if not isinstance(n, int):
        print('Factorial solo está definido para int.')
        return None
    elif n < 0:
        print('Factorial solo está definido para números positivos.')
        return None
        
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
