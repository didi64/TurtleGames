# configure movable turtles
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

invader_config = {'shape':'circle',
                 'size':(1,1), 
                 'color': 'black', 
                 'pendown': False,
                 'angle': 270
                 }

 
game_vars  ={'score': 0, 
             'level': 1, 
             'maxlevel': 10, 
             'delay': 100, 
             'speedup': 0.5, 
             'shots': 3,
             } 


config = {'score_pos1': (50, 150), 
          'score_pos2': (150, 150), 
          'level_pos': (-150,150),
          'gameover_pos': (0,200),
          'highscore_pos': (0,200),
          'bob_speed': 10,
          'ball_speed': 10,
          'error': 10,
          'left': -150,
          'right': 150,
          'top': 150,
          'bottom': -150}   