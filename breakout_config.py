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
                'pos': (0, -135),
                'angle': 37
               }

invader_config = {'shape':'turtle',
                  'size':(1,1), 
                  'color': 'black'
                 }

 
game_vars  ={'score': 0, 
             'level': 1, 
             'maxlevel': 10, 
             'delay': 10, 
             'speedup': 0.5, 
             'shrink': 0.8,
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