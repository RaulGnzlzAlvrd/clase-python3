def do_twice(f, v):
    f(v)
    f(v)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

def draw_line(symbol, separator, times):
    line = ((symbol + separator * 4) * times) + symbol
    print(line)

def do_top(times):
    draw_line('+', '-', times)

def do_body_part(times):
    draw_line('|', ' ', times)

def do_body(times):
    do_four(do_body_part, times)

def do_section(times):
    do_top(times)
    do_body(times)

def do_full(f, times):
    f(do_section, times)
    do_top(times)

do_full(do_twice, 2)
do_full(do_four, 4)
