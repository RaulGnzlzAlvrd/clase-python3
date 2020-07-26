"""
factorial n
    0! = 1
    n! =  n * n-1!
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result

factorial(1.5)

"""
factorial(3)
-------------------------
|   n = 3
|   if n == 0:
|       return 1
|   else:
|       recurse = factorial(n - 1)
                  ---------------------
                  | n = 2
                  | if n == 0:
                  |     return 1
                  | else:
                  |     recurse = factorial(n - 1)
                                  ---------------------
                                  | n = 1
                                  | if n == 0:
                                  |     return 1
                                  | else:
                                  |     recurse = factorial(n - 1)
                                                  ---------------------
                                                  | n = 0
                                                  | if n == 0:
                                                  |     return 1
                                                  | else:
                                                  |     recurse = factorial(n - 1)

                                                  |     result = n * recurse
                                                  |     return result
                                                  ---------------------
                                  |     result = n * recurse
                                  |     return result
                                  ---------------------
                  |     result = n * recurse
                  |     return result
                  ---------------------
|       result = n * recurse
|       return result
-------------------------
"""

"""
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib1 = fibonacci(n - 1)
        fib2 = fibonacci(n - 2)
        result = fib1 + fib2
        return result
