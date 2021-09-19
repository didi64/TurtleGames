import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th

def reload():
    global shots
    shots = 3

# callbacks for keypress events Left, Right and space
def bob_left():
    if  bob.running:
        bob.setheading(180)

def bob_right():
    if bob.running:
        bob.setheading(0)
    
def bob_shoot():
    global shots
    if  shots == 0: return
    shots = shots - 1
    pos = bob.pos()
    
    bullet = mTurtle(angle = 90, pos=pos, **bullet_config)
    bullet.add_action(lambda: bullet.forward(10))
    bullet.add_action(lambda: is_invader_hit(bullet))

def shoot(t):
    x = random.randint(0,100)
    if x == 0:
        pos = t.pos()
        bullet = mTurtle(angle = 270, pos=pos, **bullet_config)
        bullet.add_action(lambda: bullet.forward(10))
        bullet.add_action(lambda: is_bob_hit(bullet))

def stop_all():
    for t in invaders + [bob]:
        t.stop()

def bobs_action():
    '''move forward, check if game is won or lost'''
    bob.forward(5)
    for t in invaders:
        x,y = t.pos()
        if  y <= -150:
            stop_all()
            break
    if  invaders == []:
        stop_all()

def is_invader_hit(bullet):
    '''check if a invader is hit. If so remove it'''
    x = bullet.pos()
    for t in invaders:
        y = t.pos()
        if  th.distance(x,y) < 10:
            t.stop()
            t.remove()
            invaders.remove(t)

def is_bob_hit(bullet):
    '''check if bob is hit, if so end game'''
    x = bullet.pos()
    y = bob.pos()
    if  th.distance(x,y) < 10:
            stop_all()
            
# configure movable turtles
bob_config = {'shape':'turtle',
              'size':(1,1), 
              'color': 'blue', 
              'pendown': False,
              'pos': (0,-150)
              }

bullet_config = {'shape':'circle',
                 'size':(.1,.1), 
                 'color': 'red', 
                 'pendown': False, 
                 'maxdist': 300}

invader_config = {'shape':'circle',
                 'size':(1,1), 
                 'color': 'black', 
                 'pendown': False,
                 'angle': 270
                 }
# number of shots before reload
shots = 3

# set up screen
screen = th.screen('Hit the invaders')
bob =  mTurtle(**bob_config)   
bob.add_action(bobs_action)
invaders = [mTurtle(pos=(x,150), **invader_config) for x in range(-100,120,20)]

for t in invaders:
    t.add_action(lambda x=t: t.forward(1))
    t.add_action(lambda x=t: shoot(x))
screen.update()

# add keybindings
screen.onkeypress(bob_left, 'Left')
screen.onkeypress(bob_right, 'Right')
screen.onkeypress(reload, 'Down')
screen.onkeypress(bob_shoot, 'space')

# start actions of all movable Turtles
mTurtle.update(screen, delay= 100)
turtle.done()