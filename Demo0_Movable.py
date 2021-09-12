import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th
 
def bobs_action1():
    bob.forward(5)
    x, y = bob.pos()
    if  abs(x) >= 100:
        bob.left(90) 
    
# called if key 'space' is pressed
def start_stop():
    if bob.running:
        bob.stop()
    else:
        bob.start()     

# configure movable turtles
turtle_config = {'shape':'turtle',
                 'size':(1,1), 
                 'color': 'blue', 
                 'pendown': True,
                 'angle': 0
                 }

# set up screen that is listening for events
screen = th.screen(title='Demo Movable Turtles')

bob = mTurtle(**turtle_config)
bob.add_action(bobs_action1)

screen.onkeypress(start_stop,'space') 

# excecute actions of all mTurtle objects every delay milliseconds
mTurtle.update(screen, delay= 100)
turtle.done()  