def stones_in_col(pts, i):
    '''Wieviele Punkte in i-ter Spalte,
       1. Koordinate immer gleich X[i]
    '''
    l = [pt for pt in pts if pt[0] == X[i]]
    return l

def stones_in_row(pts, i):
    '''Wieviele Punkte in i-ten Zeile,
       2. Koordinate immer gleich X[i]
    '''
    l = [pt for pt in pts if pt[1] == X[i]]
    return l

def stones_in_diag(pts, i):
    '''Wieviele Steine in Hauptdiag (0) 
       oder Nebendiag (1)
    '''
    sign = 2*i -1   
    l = [pt for pt in pts if pt[0] == sign *pt[1]]
    return l

def is_tiktak(pts):
    '''teste ob pts tiktak enthalten'''
    l = [len(stones_in_diag(pts, i)) for i in range(3)] +\
        [len(stones_in_row(pts, i))  for i in range(3)] +\
        [len(stones_in_col(pts, i))  for i in range(3)]
    return 3 in l

def get_threats(pts, free):
    return [pt for pt in free if is_tiktak(pts+[pt])]