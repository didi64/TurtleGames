import time
from datetime import datetime

import turtle
import turtle_helpers as th
import corners as game
import time
from datetime import datetime

def place_stone(x,y, color):
    '''place a stone on screen at (x,y) with given color'''
    stone = turtle.Turtle('circle')
    stone.shapesize(2) 
    th.fly_to(stone, x, y)
    stone.color(color)
    stones.append(stone)
    # init(stone)

    buffer.append((x,y,color))
    # noetig, screen ist so konfiguriert
    screen.update() 

def init(t, x=0, a=0, c=0):
    
    if a == 0:
        a,b,c = t.shapesize()
        x=3/5*a
    x += a/5
    t.shapesize(x,x,c) 
    screen.update()
    if  x < a:
        turtle.ontimer(lambda:init(t,x,a,c), 50)
   
def play(x,y):
    '''play stone at (x,y) if this is a legal move'''
    if not running: return
    ptm = game.ptm # player to move
    # finde Punkt in coords der am naechten bei (x,y) liegt
    pos = th.closest_pt((x,y), coords)
    # falls der Zug moeglich ist, werden die
    # Variabeln in game entsprechend geaendernt
    # und True zurueckgegeben.
    was_legal =  game.play(pos)
    if  was_legal:
        # der Zug war legal, wir koennen ihn darstellen
        place_stone(*pos, colors[ptm])
        # falls Spiel zu Ende, zeige Gewinner
        if game.result is not None: 
            display_result()
        compi_move()

def display_result():
    '''display the game result'''
    

    if game.result == 'draw': msg = 'Draw\n'
    else: msg = 'Player ' + colors[game.result] + ' wins!\n'
    msg1 =  'Press "n" for new game or "m" for menu.'
    
    th.write(alice, (0,170), msg + msg1)
    screen.update() 

    
    buffer.append(str(game.result))
    #print('buffer',buffer)
    log.extend([buffer.copy()])
    buffer.clear()
    #print('log',log)

    if  game.result is True:
        score[0] += 1
    elif game.result is False:
        score[1] += 1
    elif game.result == 'draw':
        score[0] += 1
        score[1] += 1

def new_game():
    global running
    if not running: return
    running = True

    
    if buffer:
        buffer.append('None')
        log.extend([buffer.copy()])
        buffer.clear()
    # datetime object containing current date and time
    dt = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = dt.strftime('%d/%m/%Y %H:%M:%S')
    buffer.append(dt_string)


    game.new_game()
    clear_screen()
    compi_move()

def clear_screen():
    alice.clear() # delete alice's writings
    remove_stones()

def remove_stones():
    for s in stones:
        s.hideturtle()
    stones.clear()
    screen.update()

##########################################

def compi_move():
    if  computer_player is not None and \
        game.ptm == computer_player and game.result is None:
        time.sleep(0.2)
        pt = game.select_move()
        play(*pt)

def show_menu():
    global running
    alice.clear()
    running = False
    mesg = 'Press "r" to play red, "b" to play blue, "2" to play both sides.\n' + \
           '"m" for this menu, "c" to continue, "n" for new game\n' \
           '"d" to display score, "e" to reset score,\n' \
           '"l" to show logged games,"q" to quit.'     

    th.write(alice, (0,160), mesg, font = ('Arial', 15))

def start_game(cp):
    global running, computer_player
    if running: return
    else:
        alice.clear()
        computer_player = cp
        running = True
        new_game()

def replay():
    if log == []:
        print('No games logged!')
        return
    for i,line in enumerate(log):
        print(i+1,str(line))
    i = input('Game number: ')
    i = int(i) - 1
    if i < len(log):
        clear_screen()
        game = log[i]
        th.write(alice,(0,180), 'Replaying game from\n' + game[0])
        for t in game:
            if type(t) == tuple:
               time.sleep(0.4) 
               place_stone(*t)
              
def reset_score():
    score[0]=0
    score[1]=0
    display_score()

def display_score(): 
    alice.clear()
    th.write(alice, (0,180),'Current score:\n' + \
        'red: {}, blue: {}'.format(score[0], score[1] ))
    time.sleep(1)
    alice.clear()

def cont_game():
    global running
    alice.clear()
    running = True

computer_player = None
running = False
buffer = []
log = []
score = [0,0]
# set up screen
screen = th.screen(title='Play at top right to win', width=600, height=600)

# bob is our drawing turtle
bob = turtle.Turtle() 
bob.hideturtle()
# alice is our writing turtle
alice = turtle.Turtle()
alice.hideturtle()

coords = game.pts_player.keys() # coords where one can place a stone
colors = {True: 'red', False: 'blue'}
stones = [] # Liste der gesetzten Steine

# draw a tiny circle at pts in coords
th.draw_points(bob, coords) 
screen.update()

# bind functions to events
screen.onclick(play)   
screen.onkeypress(new_game, 'n')
screen.onkeypress(lambda: start_game(True), 'b')
screen.onkeypress(lambda: start_game(False), 'r')
screen.onkeypress(lambda: start_game(None), '2')
screen.onkeypress(display_score, 'd')
screen.onkeypress(reset_score, 'e')
screen.onkeypress(replay, 'l')
screen.onkeypress(show_menu, 'm')
screen.onkeypress(cont_game, 'c')
screen.onkeypress(turtle.bye, 'q')



show_menu()

turtle.done()