import math

def square_root(a):
    epsilon = 0.000001
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return x
        x = y

def print_test(n, aprox, exact, error):
    format = "%i %.5f %.5f " + str(error)
    print(format % (n, aprox, exact))

def test_square_root(n):
    x = 1.0
    while x <= n:
        aprox = square_root(x)
        exact = math.sqrt(x)
        error = abs(exact - aprox)
        print_test(x, aprox, exact, error)
        x = x + 1

test_square_root(9)
