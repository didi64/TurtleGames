import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th

def random_walk(t):
    '''turtle t wechselt zufaellig die Richting und
       bewegt sich vorwaerts'''
    x = random.randint(-1,1) 
    t.left(45*x)
    t.forward(5)  

def remove(t):
    '''turtle t wird geloescht
       falls zuweit links unten
    '''
    x,y = t.pos()
    if x <-50 and y < -50:
        t.remove(delete=False)

def stop(t):
    '''turtle t wird gestoppt
       falls zuweit rechts oben
    '''
    x,y = t.pos()
    if x > 50 and y > 50:
        t.stop()
        t.color('black')

# configure movable turtles
turtle_config = {'shape':'turtle',
                 'size':(1,1), 
                 'color': 'blue', 
                 'pendown': True,
                 'maxdist': 150
                 }

# set up screen that is listening for events
screen = th.screen(title='Demo Movable Turtles')

# turtle alice draws some bounderies
alice = turtle.Turtle()
alice.color('red')
th.fly_to(alice,0,-150)
alice.circle(150)
th.connect_points(alice, [(-250,-50),(-50,-50),(-50,-250)])
th.connect_points(alice, [(250,50),(50,50),(50,250)])
# screen.update()

# create movable turtles
for i in range(10):
    angle = random.randint(0,360)
    mt = mTurtle(angle = angle, **turtle_config)
    mt.add_action(lambda t=mt: random_walk(t))
    mt.add_action(lambda t=mt: stop(t))
    mt.add_action(lambda t=mt: remove(t))
    
# excecute actions of all mTurtle objects every delay milliseconds
mTurtle.update(screen, delay= 50)
turtle.done()  