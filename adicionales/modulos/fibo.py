"""Fibonacci numbers module"""

def fib(n):
    """Print the fibonacci sequence until n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=100):
    """Return a list with the fibonacci sequence until n."""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
