from swampy.TurtleWorld import *

from rectangles import Rectangle
from points import Point
from circles import Circle
from polygon import circle as d_circle

def draw_rect(turtle, rectangle):
    turtle.heading = 0
    turtle.x = rectangle.corner.x
    turtle.y = rectangle.corner.y
    turtle.pd()

    for i in range(2):
        turtle.fd(rectangle.width)
        turtle.lt(90)
        turtle.fd(rectangle.height)
        turtle.lt(90)

def draw_circle(turtle, circle):
    turtle.x = circle.center.x
    turtle.y = circle.center.y - circle.radius
    turtle.heading = 0
    turtle.pu()
    turtle.pd()
    d_circle(turtle, circle.radius)

def main():
    world = TurtleWorld()
    bob = Turtle()
    bob.delay = 0.01

    box = Rectangle()
    box.width = 50
    box.height = 60
    box.corner = Point()
    box.corner.x = 50
    box.corner.y = 50

    draw_rect(bob, box)

    c = Circle()
    c.center = Point()
    c.center.x = 50
    c.center.y = 50
    c.radius = 25

    draw_circle(bob, c)

    wait_for_user()

if __name__ == "__main__":
    main()
