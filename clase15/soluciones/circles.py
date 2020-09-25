from points import Point, distance
from rectangles import Rectangle, get_corners

class Circle:
    """ Representa un círculo

    atributos:
        center: Point
        radius: number
    """

def point_in_circle(circle, point):
    return distance(point, circle.center) <= circle.radius

def rectangle_in_circle(circle, rectangle):
    corners = get_corners(rectangle)
    for corner in corners:
        if not point_in_circle(circle, corner):
            return False
    return True

def rectangle_circle_overlaps(circle, rectangle):
    corners = get_corners(rectangle)
    for corner in corners:
        if point_in_circle(circle, corner):
            return True
    return False

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

if __name__ == "__main__":
    main()
