from swampy.TurtleWorld import *
import math

def square(t, length):
    '''
    Dibuja un cuadrado con una tortuga
    t : Turtle
    length : float
    '''
    polygon(t, length, 4)

def polygon(t, length, n):
    angle = 360 / n
    poly_line(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r / 360 * angle
    lados = int(arc_length / 3) + 1
    length = arc_length / lados
    step_angle = angle / lados
    poly_line(t, lados, length, step_angle)

def poly_line(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
