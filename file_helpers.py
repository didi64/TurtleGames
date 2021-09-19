def readlines(fn):
    try:
        with open(fn, 'r', encoding='utf8') as f:
            lines = f.readlines()
    except (OSError, FileNotFoundError):
        lines = []
    lines = [line.rstrip() for line in lines] 
    return lines  

def writelines(fn, lines):
    with open(fn, 'w', encoding='utf8') as f:
        f.writelines([line + '\n' for line in lines[:-1]])
        f.writelines([lines[-1]])

def get_highscores(fn):
    hs = readlines(fn)
    return  [line.split(',') for line in hs] 
    
def is_highscore(score, fn):
    hs = readlines(fn)
    hs_t =  [line.split(',') for line in hs] 
    return len(hs) < 3 or score > int(hs_t[-1][1])
    
def update_scores(name, score, fn):   
    hs_t =  get_highscores(fn)
    hs_t.append((name, score))
    hs_t.sort(key = lambda x: int(x[1]), reverse =True) 
    hs = ['{},{}'.format(t[0], t[1]) for t in hs_t[:3]]
    writelines(fn, hs)

def update_scores_(name, score, fn):   
   
    hs = readlines(fn)
    hs_t =  [line.split(',') for line in hs]  
    
    if  len(hs) < 3 or score > int(hs_t[-1][1]):
        hs_t.append((name, score))
        hs_t.sort(key = lambda x: int(x[1]), reverse =True) 
        hs = ['{},{}'.format(t[0], t[1]) for t in hs_t[:3]]
        writelines(fn, hs)