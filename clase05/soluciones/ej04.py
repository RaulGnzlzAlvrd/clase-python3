from swampy.TurtleWorld import *

def koch(t, length):
    if length < 3:
        fd(t, length)
        return
    new_length = length / 3
    koch(t, new_length)
    lt(t, 60)
    koch(t, new_length)
    rt(t, 120)
    koch(t, new_length)
    lt(t, 60)
    koch(t, new_length)

def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        rt(t, 120)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

snowflake(bob, 100)

wait_for_user()
