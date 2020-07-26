from swampy.TurtleWorld import *
import polygon

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

polygon.polygon(bob, n=8, length=50)

wait_for_user()
