import math

class Point:
    """ Representación de un punto en un espacio 2D """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """ Imprime las coordenadas del punto """
        return "(%g, %g)" % (self.x, self.y)

    def distance(self, other):
        """ Regresa la distancia entre el punto y other """
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def __add__(self, other):
        if other == 0:
            other = Point()
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def add_tuple(self, t):
        x = self.x + t[0]
        y = self.y + t[1]
        return Point(x, y)

if __name__ == "__main__":
    p1 = Point(3, 4)
    print(p1)

    origin = Point()
    print(origin)

    print("Distance: %g" % p1.distance(origin))

    print(p1 + origin + Point(1,1))

    print((5,6) + p1)

    print(sum([p1,origin, (1,2)]))
