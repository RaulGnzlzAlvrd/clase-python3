import math

class Point:
    """ Representación de un punto en un espacio 2D """

def print_point(p):
    print("(%g, %g)" % (p.x, p.y))

def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)


if __name__ == "__main__":
    p1 = Point()
    p1.x = 3
    p1.y = 4

    print_point(p1)

    origin = Point()
    origin.x = 0
    origin.y = 0

    print_point(origin)

    print("Distance: %g" % distance(p1, origin))
