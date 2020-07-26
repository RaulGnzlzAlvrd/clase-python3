from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print(bob)

def square(t, length):
    polygon(t, length, 4)

def polygon(t, length, n):
    angle = 360 / n
    poly_line(t, length, n, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r / 360 * angle
    n = int(arc_length / 3) + 1
    step_angle = angle / n
    step_length = arc_length / n
    poly_line(t, step_length, n, step_angle)

def poly_line(t, length, n, angle):
    """Dibuja segmentos de línea de un tamaño y ángulo específico.

    t : Turtle
        La tortuga que va a dibujar los segmentos
    length : float
        La longitud de cada segmento dibujado
    n : int
        La cantidad de segmentos a dibujar
    angle : float
        El ángulo (en grados) entre cada segmento
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def radians(degrees):
    return degrees / 360 * 2 * math.pi

def degrees(radians):
    return 360 * radians / 2 / math.pi

arc(bob, r=50, angle=degrees(math.pi))

wait_for_user()
