import time
import turtle
import turtle_helpers as th
import tiktak as game

def place_stone(x,y, color):
    '''place a stone on screen at (x,y) with given color'''
    stone = turtle.Turtle('circle')
    stone.shapesize(2) 
    th.fly_to(stone, x, y)
    stone.color(color)
    stones.append(stone)
    # noetig, screen ist so konfiguriert
    screen.update() 

def play(x,y):
    '''play stone at (x,y) if this is a legal move'''
    if not game_vars['running']: return
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
    alice.clear()
    if game.result == 'draw': 
        msg = 'Draw\n'
    else: 
        msg = 'Player ' + colors[game.result] + ' wins!\n'
    msg1 =  'Press "n" for new game or "m" for menu.'
    
    th.write(alice, (0,170), msg + msg1)
    screen.update() 
    
def new_game():
    cont_game()
    game.new_game()
    clear_screen()
    show_mode()
    compi_move()

def show_mode():
    alice.clear()
    cp = game_vars['computer_player']
    if  cp is None:
        th.write(alice,(0,200),'2 Player Mode')

    else:
        th.write(alice,(0,200),'You play with '+colors[not cp])
def clear_screen():
    alice.clear() 
    remove_stones()

def remove_stones():
    for s in stones:
        s.hideturtle()
    stones.clear()
    screen.update()

##########################################
def compi_move():
    if  game_vars['computer_player'] is not None and \
        game.ptm == game_vars['computer_player'] and \
            game.result is None:
        time.sleep(0.2)
        pt = game.select_move()
        play(*pt)

def start_game(cp):
    if game_vars['running']: return
    else:
        game_vars['computer_player'] = cp
        new_game()

######################
def show_menu():
    alice.clear()
    pause_game()
    mesg = 'Press "r" to play red, "b" to play blue, "2" to play both sides.\n' + \
           '"m" for this menu, "c" to continue, "n" for new game\n' \
           '"d" to display score, "e" to reset score,\n' \
           '"p" to show logged games,"q" to quit.'     

    th.write(alice, (0,160), mesg, font = ('Arial', 15))

def reset_score():
    game.reset_score()
    
def display_score(): 
    score =game.score
    alice.clear()
    th.write(alice, (0,180),'Current score:\n' + \
        'red: {}, blue: {}'.format(score[0], score[1] ))
    time.sleep(1)
    alice.clear()

def pause_game():
    game_vars['running'] = False

def cont_game():
    show_mode()
    game_vars['running'] = True

##########################
def replay():
    if game.log == []:
        print('No games logged!')
        return

    for i,line in enumerate(game.log):
        print(i+1,str(line))
    i = input('Game number: ')
    i = int(i) - 1
    if i < len(game.log):
        clear_screen()
        pause_game()
        game_log = game.log[i]
        th.write(alice,(0,180), 'Replaying game from\n' + game_log[0])
        for t in game_log:
            if type(t) == tuple:
               time.sleep(0.4) 
               x,y,p = t
               place_stone(x,y,colors[p])


# game Variables
game_vars = {'running': False, 'computer_player': None}

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
screen.onkeypress(replay, 'p')
screen.onkeypress(show_menu, 'm')
screen.onkeypress(cont_game, 'c')
screen.onkeypress(turtle.bye, 'q')



show_menu()

turtle.done()