def do_twice(f, v):
    f(v)
    f(v)

def print_twice(s):
    do_twice(print, s)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

do_twice(print_twice, "spam")
do_four(print_twice, "spam")
