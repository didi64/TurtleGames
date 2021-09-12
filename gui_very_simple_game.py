import turtle
import turtle_helpers as th
import game1 as game

def place_stone(x,y, color):
    '''place a stone on screen at (x,y) with given color'''
    stone = turtle.Turtle('turtle')
    th.fly_to(stone, x, y)
    stone.color(color)
    stones.append(stone)
    screen.update()

def play(x,y):
    '''play stone at (x,y) if this is a legal move'''
    ptm = game.ptm # player to move
    pos = th.closest_pt((x,y), coords)
    was_legal =  game.play(pos)
    if  was_legal:
        place_stone(*pos, colors[ptm])
        if game.result is not None: 
            display_result()

def display_result():
    '''display the game result'''
    th.write(alice, (0,170), str(game.result) + '\nPress n for new game')
    screen.update() 

def new_game():
    game.new_game()
    alice.clear() # delete alice's writings
    for s in stones:
        s.hideturtle()
    stones.clear()
    screen.update()

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
stones = []

th.draw_points(bob, coords) # draw a tiny circle at pts in coords
screen.update()
# bind functions to events
screen.onclick(play)   
screen.onkeypress(new_game,'n')

turtle.done()