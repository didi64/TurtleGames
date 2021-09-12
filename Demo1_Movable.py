import random
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th

def bobs_action1():
    bob.forward(5)
    x, y = bob.pos()
    if  abs(x) >= 100:
        bob.left(90) 
    
def bobs_action2():
    d = bob.dist()
    if d > 50:
        bob.color('red')
    else:
        bob.color('blue')    

def bobs_action3():
    '''schreibe bob's Distanz von seinem Ursprung
       bei jedem zweiten Aufruf von bobs_action3
    '''
    d = int(bob.dist())
    count = bob.action_counter[bobs_action3]
    if  count % 2== 0:
        alice.clear()
        th.write(alice, (0, 150), str(d))

# callbacks
# called if key 'space' is pressed
def start_stop():
    if bob.running:
        bob.stop()
    else:
        bob.start()   

# called if key 'r' is pressed          
def remove_with_drawings():
    bob.remove()
    print('Bob is now  untracked')

# called if key 'd' is pressed      
def remove_without_drawings():
    bob.remove(delete=False)
    print('Bob is now  untracked')
    
# called if key 't' is pressed
def track_untrack():
    if bob.is_tracked():
        bob.track(False)
        print('Bob is now  untracked')
    else:
        bob.track(True)   
        print('Bob is tracked again')

# configure movable turtles
turtle_config = {'shape':'turtle',
                 'size':(1,1), 
                 'color': 'blue', 
                 'pendown': True,
                 'angle': 0
                 }

# set up screen that is listening for events
screen = th.screen(title='Demo Movable Turtles')

alice=turtle.Turtle()
alice.hideturtle()

bob = mTurtle(**turtle_config)
bob.add_action(bobs_action1)
bob.add_action(bobs_action2)
bob.add_action(bobs_action3)
    
screen.onkeypress(start_stop,'space')  
screen.onkeypress(remove_with_drawings,'r') 
screen.onkeypress(remove_without_drawings,'d') 
screen.onkeypress(track_untrack,'t') 

# excecute actions of all  tracked  mTurtle objects t 
# with t.running = True every delay milliseconds
mTurtle.update(screen, delay= 100)
turtle.done()  