import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th

# callbacks for keypress events Left, Right and space
def bob_left():
    if  bob.running:
        bob.setheading(180)

def bob_right():
    if bob.running:
        bob.setheading(0)
    
def stop_all():
    for t in  + [bob, ball]:
        t.stop()

def bobs_action():
    '''move forward, check if game is won or lost'''
    bob.forward(5)
    x,y = bob.pos()
    # change bob's direction if he hits an edge
    if x >= 150: bob.setheading(180)
    if x <= -150: bob.setheading(0)
    # stoppe bob und ball falls alle invaders getroffen
    if  invaders == []: stop_all()

def is_invader_hit():
    '''check if a invader is hit. If so remove it'''
    x = ball.pos()
    for t in invaders:
        y = t.pos()
        if  th.distance(x,y) < 10:
            t.remove()
            invaders.remove(t)

def reflect(t,side=True):
    c = 180 if side else 360
    angle = t.heading()
    angle = c - angle
    t.setheading(angle) 
    
def balls_action():
    '''check if bob catches the ball'''
    ball.forward(5)
    is_invader_hit()
    x0, y0 = bob.pos()
    x1, y1 = ball.pos()
    width_bob = bob.shapesize()[1] * 20
    
    # check if bob catches the ball
    if  (abs(y0 - y1) <= 5 and abs(x0 - x1) < width_bob/2):
        reflect(ball, side=False)
    if y1 >= 150:
        reflect(ball, side=False)
    if abs(x1) >= 150:
        reflect(ball, side=True)
    
# wird bei druecken von 'space' ausgefuehrt
def start_stop():
    if ball.running: ball.stop()
    else: ball.start()   
#######################################    
# configure movable turtles
bob_config = {'shape':'square',
              'size':(0.3,6), # height=0.3*20px, width=6*20px
              'color': 'blue', 
              'pendown': False,
              'pos': (0,-150)
              }

ball_config = {'shape':'circle',
                'size':(.3,.3), 
                'color': 'magenta', 
                'pendown': False, 
                'pos': (0,-135),
                'angle': 37
               }

invader_config = {'shape':'turtle',
                  'size':(1,1), 
                  'color': 'black'
                 }
# set up screen that listens for events,
# gezeichnet wird beim Aufruf von screen.update()
screen = th.screen('Hit the invaders')
bob =  mTurtle(**bob_config)   
bob.add_action(bobs_action)
invaders = [mTurtle(pos=(x,120), **invader_config) for x in range(-100,120,20)]
ball = mTurtle(**ball_config)
ball.add_action(balls_action)

# turtle alice zeichnet die Spielfeldberandung
alice = turtle.Turtle()
alice.hideturtle()
th.draw_square_from(alice,(-150,-150),300)

# add keybindings
screen.onkeypress(bob_left, 'Left')
screen.onkeypress(bob_right, 'Right')
screen.onkeypress(start_stop, 'space')

# execute actions of all movable Turtles t on screen t with
# t.running == True every delay milliseconds. 
# Then  screen.update() is called.
mTurtle.update(screen, delay = 30)
turtle.done()