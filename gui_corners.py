import turtle
import turtle_helpers as th
import corners as game
import time
def place_stone(x,y, color):
    '''place a stone on screen at (x,y) with given color'''
    stone = turtle.Turtle('turtle')
    th.fly_to(stone, x, y)
    stone.color(color)
    stones.append(stone)
    # noetig, screen ist so konfiguriert
    screen.update() 

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
    msg = 'Player ' + colors[game.result] + ' wins!\n' + \
          'Press "n" for new game or "m" for menu.'
    th.write(alice, (0,170), msg)
    screen.update() 

def new_game():
    global running
    if not running: return
    running = True
    game.new_game()
    alice.clear() # delete alice's writings
    for s in stones:
        s.hideturtle()
    stones.clear()
    screen.update()
    compi_move()
##########################################

def compi_move():
    if  computer_player is not None and game.ptm == computer_player:
        time.sleep(0.2)
        pt = game.select_move()
        play(*pt)

def show_menu():
    global running
    alice.clear()
    running = False
    mesg = 'Press "r" to play red, "b" to play blue.\n' + \
           'Press "Enter" to play both sides.\n' + \
           'Press "m" for this menu.\n' + \
           'To play: leftclick on a point.'

    th.write(alice, (0,170), mesg, font = ('Arial', 10))

def start_game(cp):
    global running, computer_player
    if running: return
    else:
        alice.clear()
        computer_player = cp
        running = True
        new_game()

computer_player = None
running = False

# set up screen
screen = th.screen(title='Play at top right to win')

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
screen.onkeypress(lambda: start_game(None), 'Return')
screen.onkeypress(show_menu, 'm')
screen.onkeypress(turtle.bye, 'q')

show_menu()

turtle.done()