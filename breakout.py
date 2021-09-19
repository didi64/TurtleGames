import random
import time
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th
import file_helpers as F
import breakout_config as C

# callbacks for keypress events Left, Right and space
def new_game():
    mTurtle.pause()
    game_vars.update(C.game_vars)
    clear_screen()
    th.draw_square_from(alice,(-150,-150), 300)
    th.write(alice, C.config['score_pos1'], 'Score: ',align = 'right')
    start_level()
     
def bob_left():
    if  bob.running:
        bob.setheading(180)

def bob_right():
    if bob.running:
        bob.setheading(0)
    
def bobs_action():
    '''move forward, check if game is won or lost'''
    bob.forward(C.config['bob_speed'])
    x,y = bob.pos()
    # change bob's direction if he hits an edge
    if x >= C.config['right']: bob.setheading(180)
    if x <= C.config['left']: bob.setheading(0)
    # stoppe bob und ball falls alle invaders getroffen
    if  invaders == []: 
        next_level()
        time.sleep(1)
        start_level() 

def autoplay():
    x,y = ball.pos()
    x0,y0 = bob.pos()
    bob.goto(x,y0)        

def is_invader_hit():
    '''check if a invader is hit. If so remove it'''
    x = ball.pos()
    for t in invaders:
        y = t.pos()
        if  th.distance(x,y) < C.config['error']:
            t.remove()
            invaders.remove(t)
            game_vars['score'] += 10 * game_vars['level']
            ball.setheading(random.randint(1, 30) *13)
            update_score()

def reflect(t,side=True):
    c = 180 if side else 360
    angle = t.heading()
    angle = c - angle
    t.setheading(angle) 
    
def balls_action():
    '''check if bob catches the ball'''
    ball.forward(C.config['ball_speed'])
    is_invader_hit()
    x0, y0 = bob.pos()
    x1, y1 = ball.pos()
    width_bob = bob.shapesize()[1] * 20
    
    # check if bob catches the ball
    if  (abs(y0 - y1) <= 5 and abs(x0 - x1) < width_bob/2):
        reflect(ball, side=False)
    if y1 >= C.config['top']:
        reflect(ball, side=False)
    if abs(x1) >= C.config['top']:
        reflect(ball, side=True)
    if  y1 < C.config['bottom'] - C.config['error']:
        game_over()

def game_over():
    mTurtle.pause()
    th.write(alice, C.config['gameover_pos'], 'Game over!')
    time.sleep(2)
    high_scores()
    display_high_scores()

def high_scores():   
    score = game_vars['score']
    if F.is_highscore(score, 'high_scores.txt'):
        name = get_name()
        F.update_scores(name, score, 'high_scores.txt')

def get_name():       
    name = input('Enter your name: ')
    return name

def display_high_scores():
    clear_screen()
    hst =  F.get_highscores('high_scores.txt') 
    x, y = C.config['highscore_pos']
    th.write(alice, (x,y), 'High Score List')
    for i,(name, pts) in enumerate(hst):
        th.write(alice, (0, y - 60 - i * 40), '{}:{}'.format(name, pts))

# wird bei druecken von 'space' ausgefuehrt
def start_stop():
    if ball.running: ball.stop()
    else: ball.start()   

def update_score():
    carl.clear()
    th.write(carl, C.config['score_pos2'], str(game_vars['score']), align='right')

def clear_screen():
    clear_invaders()
    for t in [alice, carl, dan]:
        t.clear()


def clear_invaders():
    for t in invaders: t.remove() # untrack and hide
    invaders.clear()

def reset_invaders(level):
    clear_invaders()
    ml = min(game_vars['level'],  game_vars['maxlevel'])
    for x in  range(-100,120,20):
        for i in range(ml):
            mt = mTurtle(pos=(x,120-(i-1)*20), **C.invader_config)
            invaders.append(mt)
    
def next_level():
    game_vars['level'] += 1
    game_vars['delay'] *= game_vars['speedup'] 
    h,w,s = bob.shapesize()
    w *= game_vars['shrink']
    bob.shapesize(h,w,s)
   

def start_level():
    reset_invaders(game_vars['level'])
    ball.goto(C.ball_config['pos'])
    ball.setheading(C.ball_config['angle'])
    bob.goto(C.bob_config['pos'])
    ball.track(True)
    bob.track(True)    

    dan.clear()
    th.write(dan, C.config['level_pos'], 'Level: ' + str(game_vars['level']), align ='left')
    
    mTurtle.set_delay(game_vars['delay'])
    mTurtle.restart()

#######################################    

game_vars = {}
invaders  = []
# set up screen that listens for events,
# gezeichnet wird beim Aufruf von screen.update()
screen = th.screen('Hit the invaders')
# alice: Spielfeldberandung, Game over
# carl: update score
# dan: writes level
alice, carl, dan = th.get_turtles(3)

bob =  mTurtle(**C.bob_config)   
bob.add_action(bobs_action)
bob.add_action(autoplay)
ball = mTurtle(**C.ball_config)
ball.add_action(balls_action)

# add keybindings
screen.onkeypress(bob_left, 'Left')
screen.onkeypress(bob_right, 'Right')
screen.onkeypress(start_stop, 'space')
screen.onkeypress(new_game, 'n')

new_game()
mTurtle.update(screen, delay = game_vars['delay'])
turtle.done()