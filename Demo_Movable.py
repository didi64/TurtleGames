import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th

def random_walk(t):
    # t has a method dist, and an attribute maxdist
    x = random.randint(-1,1) 
    t.left(45*x)
    t.forward(5)  

# set up screen that is listening for events
screen = th.screen(title='Movable Turtles')

# configure movable turtles
turtle_config = {'shape':'turtle',
                 'size':(1,1), 
                 'color': (0,0,1), 
                 'pendown': True, 
                 'maxdist': 230}

def random_walk(t):
    # t has a method dist, and an attribute maxdist
    x = random.randint(0,2) -1
    t.left(45*x)
    t.forward(5)  

for i in range(10):
    angle = random.randint(0,360)
    mt = mTurtle(angle = angle, **turtle_config)
    mt.add_action(lambda t=mt: random_walk(t))
    
# excecute actions of all mTurtle objects every delay milliseconds
mTurtle.update(screen, delay= 100)
turtle.done()  