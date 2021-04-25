import copy

from points import Point, print_point, distance

class Rectangle:
    """ Representa un rectángulo

    attributes: width, height, corner.
    """

def find_center(r):
    """ Regresa el punto central del rectángulo r """
    p = Point()
    p.x = r.corner.x +r.width / 2
    p.y = r.corner.y +r.height / 2
    return p

def grow_rectangle(rectangle, dwidth, dheight):
    """ Aumenta el tamanio del rectangle en dwidth unidades y dheight unidades """
    rectangle.width += dwidth
    rectangle.height += dheight

def move_rectangle(rectangle, dx, dy):
    """ Regresa un rectangulo desplazando rectangle dx unidades al eje x y dy unidades en el eje y """
    moved = copy.deepcopy(rectangle)
    moved.corner.x += dx
    moved.corner.y += dy
    return moved

def get_corners(rectangle):
    """ Regresa los puntos de las esquinas de rectangle """
    t = [0] * 4
    for i in range(4):
        t[i] = Point()
    corner = rectangle.corner
    width = rectangle.width
    height = rectangle.height
    x = corner.x
    y = corner.y

    t[0].x = x
    t[0].y = y
    t[1].x = x + width
    t[1].y = y
    t[2].x = x
    t[2].y = y + height
    t[3].x = x + width
    t[3].y = y + height

    return t

if __name__ == "__main__":
    box = Rectangle()
    box.width = 100
    box.height = 200
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0

    center = find_center(box)
    print_point(center)
    print(distance(center, box.corner))
