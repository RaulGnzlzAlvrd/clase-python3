import time

def countdown(n):
    if n <= 0:
        print("Kaboom!")
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)
    """
    for i in range(n):
        print(s)
    """

def funcion_rec():
    funcion_rec()


def do_n(f, n):
    if n <= 0:
        return
    else:
        f()
        do_n(f, n - 1)
