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
        bob.left(5)

def bob_right():
    if bob.running:
        bob.right(5)

def make_bullet(pos, angle, speed, f):
    '''make a bullet'''
    b = mTurtle(angle = angle, pos=pos, **bullet_config)  
    b.add_action(lambda: b.forward(speed))
    b.add_action(lambda: f(b))

def bob_shoot():
    global shots
    if  shots == 0: return
    shots = shots - 1
    pos = bob.pos()
    make_bullet(pos, bob.heading(), 10, is_invader_hit)

def shoot(t):
    x = random.randint(0,100)
    if x == 0:
        pos = t.pos() 
        for angle in range(0,360,180):
            make_bullet(pos, angle, 10, is_bob_hit)
           
def walk(t):
    x = random.randint(-10,10) 
    t.left(2*x)
    t.forward(2)  
    torus(t)

def stop_all():
    for t in invaders + [bob]:
        t.stop()

def torus(t):
    x,y = t.pos()
    x = ((x+150)% 300) - 150
    y = ((y+150)% 300) - 150
    t.goto(x,y)

def bobs_action():
    '''move forward, check if game is won or lost'''
    bob.forward(5)
    torus(bob)
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
            print('game over')
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

invader_config = {'shape':'turtle',
                 'size':(1,1), 
                 'color': 'black', 
                 'pendown': False
                 }
# number of shots before reload
shots = 3


# set up screen
screen = th.screen('Turtle Battle')
bob =  mTurtle(**bob_config)  
 
bob.add_action(bobs_action)
invaders = [mTurtle(pos=(x,y), **invader_config) \
       for x in [100,-100] for y in [100,-100]]

alice = turtle.Turtle()
alice.hideturtle()
th.draw_square_from(alice,(-150,-150),300)


for t in invaders:
    t.add_action(lambda x=t: walk(x))
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