import random
import time
import turtle
from movable_Turtle import movableTurtle as mTurtle
import turtle_helpers as th
import invaders_config as C
def new_game():
    mTurtle.pause()
    game_vars.update(C.game_vars)
    clear_screen()
    th.draw_square_from(alice,(-150,-150), 300)
    th.write(alice, C.config['score_pos1'], 'Score: ',align = 'right')
    start_level()

def update_score():
    carl.clear()
    th.write(carl, C.config['score_pos2'], str(game_vars['score']), align='right')

def reload():
    game_vars['shots'] = C.game_vars['shots']

# callbacks for keypress events Left, Right and space
def bob_left():
    if  bob.running:
        bob.setheading(180)

def bob_right():
    if bob.running:
        bob.setheading(0)
    
def bob_shoot():
    
    if  game_vars['shots'] == 0: return
    game_vars['shots'] -= 1
    pos = bob.pos()
    
    bullet = mTurtle(angle = 90, pos=pos, **C.bullet_config)
    bullet.add_action(lambda: bullet.forward(10))
    bullet.add_action(lambda: is_invader_hit(bullet))
    bullets.append(bullet)

def shoot(t):
    x = random.randint(0,100)
    if x == 0:
        pos = t.pos()
        bullet = mTurtle(angle = 270, pos=pos, **C.bullet_config)
        bullet.add_action(lambda: bullet.forward(10))
        bullet.add_action(lambda: is_bob_hit(bullet))
        bullets.append(bullet)


def bobs_action():
    '''move forward, check if game is won or lost'''
    bob.forward(5)
    for t in invaders:
        x,y = t.pos()
        if  y <= -150:
            stop_all()
            break
    if  invaders == []:
        next_level()
        time.sleep(1)
        start_level() 

def clear_screen():
    clear_invaders()
    for t in [alice, carl, dan]:
        t.clear()
    for b in bullets:
        b.hideturtle()
    bullets.clear()
    #screen.update()

def next_level():
    game_vars['level'] += 1
    game_vars['delay'] *= game_vars['speedup'] 
    game_vars['enemy_firerate'] *=1.5

def start_level():
    reset_invaders(game_vars['level'])
    bob.goto(C.bob_config['pos'])
    bob.color(C.bob_config['color'])
    bob.track(True)   
    
    dan.clear()
    th.write(dan, C.config['level_pos'], 'Level: ' + str(game_vars['level']), align ='left')
     
    mTurtle.set_delay(game_vars['delay'])
    mTurtle.restart()

def clear_invaders():
    for t in invaders: t.remove() # untrack and hide
    invaders.clear()

def reset_invaders(level):
    clear_invaders()
    # ml = min(game_vars['level'],  game_vars['maxlevel'])
    ml = 1
    for x in  range(-100,120,20):
        for i in range(ml):
            mt = mTurtle(pos=(x,120-(i-1)*20), **C.invader_config)
            invaders.append(mt)
    for t in invaders:
        t.add_action(lambda x=t: x.forward(1))
        t.add_action(lambda x=t: shoot(x))

def is_invader_hit(bullet):
    '''check if a invader is hit. If so remove it'''
    x = bullet.pos()
    for t in invaders:
        y = t.pos()
        if  th.distance(x,y) < 10:
            t.stop()
            t.remove()
            invaders.remove(t)
            game_vars['score'] += 10 * game_vars['level']
            update_score()

def is_bob_hit(bullet):
    '''check if bob is hit, if so end game'''
    x = bullet.pos()
    y = bob.pos()
    if  th.distance(x,y) < 10:
            bob.color('red')
            game_over()

def game_over():
    mTurtle.pause()
    clear_screen()

    th.write(alice, C.config['gameover_pos'], 'Game over!')
    screen.update()
    time.sleep(2)
    # high_scores()
    # display_high_scores()


# number of shots before reload

game_vars = {}
invaders = []
bullets  = []

alice, carl, dan = th.get_turtles(3)
# set up screen
screen = th.screen('Hit the invaders')
bob =  mTurtle(**C.bob_config)   
bob.add_action(bobs_action)

# add keybindings
screen.onkeypress(bob_left, 'Left')
screen.onkeypress(bob_right, 'Right')
screen.onkeypress(reload, 'Down')
screen.onkeypress(bob_shoot, 'space')
screen.onkeypress(new_game, 'n')

new_game()
# start actions of all movable Turtles
mTurtle.update(screen, delay= 100)
turtle.done()