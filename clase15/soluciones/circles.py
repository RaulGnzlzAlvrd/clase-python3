from points import Point, distance
from rectangles import Rectangle, get_corners

class Circle:
    """ Representa un círculo

    atributos:
        center: Point
        radius: number
    """

def point_in_circle(circle, point):
    """ Regresa True si point se encuentra dentro o sobre la circunferencia de circle """
    return distance(point, circle.center) <= circle.radius

def rectangle_in_circle(circle, rectangle):
    """ Regresa True si rectangle está totalmente contenido dentro de circle o en su circunferencia """
    corners = get_corners(rectangle)
    for corner in corners:
        if not point_in_circle(circle, corner):
            return False
    return True

def rectangle_circle_overlaps(circle, rectangle):
    """ Regresa True si hay alguna esquina de rectangle dentro de circle """
    corners = get_corners(rectangle)
    for corner in corners:
        if point_in_circle(circle, corner):
            return True
    return False

def rectangle_circle_overlaps_challenge(circle, rectangle):
    """ Regresa True si circle y rectangle se intersectan """

    if circle_in_rectangle_axis(circle, rectangle, 'x'):
        return True
    if circle_in_rectangle_axis(circle, rectangle, 'y'):
        return True
    for corner in get_corners(rectangle):
        if distance(circle.center, corner) <= circle.radius:
            return True
    return False

def value_in_range(value, r1, r2):
    """ Regresa True si value está entre r1 y r2

        Es decir si value es menor o igual a r2 pero mayor o igual a r2
    """
    return value >= r1 and value <= r2

def circle_in_rectangle_axis(circle, rectangle, axis):
    rx = rectangle.corner.x
    cr = circle.radius
    ry = rectangle.corner.y
    if axis == 'x':
        return value_in_range(circle.center.x, rx - cr, rx + cr + rectangle.width) and value_in_range(circle.center.y, ry, ry + rectangle.height)
    else: # axis == 'y'
        return value_in_range(circle.center.y, ry - cr, ry + cr + rectangle.height) and value_in_range(circle.center.x, rx, rx + rectangle.width)

def main():
    c = Circle()
    c.center = Point()
    c.center.x = 150
    c.center.y = 100
    c.radius = 75

    p = Point()
    p.x = 150
    p.y = 175

    print(point_in_circle(c, p))

    # Testing challenge
    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 0
    rect.corner.y = 0
    rect.height = 3
    rect.width = 5

    c = Circle()
    c.center = Point()
    c.radius = 1
    c.center.x = 5
    c.center.y = 3

    res = rectangle_circle_overlaps_challenge(c, rect)
    print(res)

if __name__ == "__main__":
    main()
