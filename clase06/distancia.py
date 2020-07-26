import math

def distance(x1, y1, x2, y2):
    return hypotenuse(x2 - x1, y2 - y1)

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def area(radio):
    temp = math.pi * radio ** 2
    return temp

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(hypotenuse(30, 40))
