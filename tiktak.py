import random
from datetime import datetime
import tiktak_helpers as H

def update_result():
    '''update result'''
    global result
    if H.is_tiktak(get_pts([True])): result = True
    elif H.is_tiktak(get_pts([False])): result = False
    elif get_pts([None]) == []: result = 'draw'
    # if game ends, log result and score
    if result is not None:
        update_score()
        update_log()

def get_pts(players):
    '''return list of positions where player in the list players have played'''
    return [pt for (pt,p) in pts_player.items() if p in players]

def is_legal(pt):
    '''check if move is illegal'''
    return  pt not in get_pts([True,False])
       
def play(pt):
    '''player plays point pt'''
    global ptm
    if result is None and is_legal(pt): 
        pts_player[pt] = ptm 
        buffer.append((*pt,ptm))
        update_result()
        ptm = not ptm
        return True 

def select_move():
    free = get_pts([None])
    winners = H.get_threats(get_pts([ptm]), free)
    threats = H.get_threats(get_pts([not ptm]), free)
    
    if winners: return winners[0]
    elif threats: return random.choice(threats)
    elif free: return  random.choice(free)
    else: print('???')
        
def new_game():
    '''start new game'''
    global ptm, result
    result = None
    ptm = True
    for pt in pts_player: 
        pts_player[pt] = None

    update_log(new=True)    


#####################
# logging

def update_log(new=False):

    if buffer:
        buffer.append(str(result))
        log.extend([buffer.copy()])
        buffer.clear()
    if new:
        dt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        buffer.append(dt)

def reset_score():
    score[0]=0
    score[1]=0      

def update_score():    
    if  result is True:
        score[0] += 1
    elif result is False:
        score[1] += 1
    elif result == 'draw':
        score[0] += 1
        score[1] += 1
  
# game variables
score = [0,0]
buffer = []
log = []
X = [-100, 0, 100] 
H.X = X # pass X to modul tiktak_helpers
pts_player = {(x,y): None for x in X for y in X}
ptm = True # player to move
result = None