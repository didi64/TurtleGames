import turtle
import math

def screen(title='Test', width=500, height=500, listen=True, tracer=0):   
    ''''set up screen:
        - listen = True: screen erkennt events wie oncklick, onkeypress,...
        - tracer = 0: gezeichnet wird erst beim Aufruf von sreen.update(),
                      dann aber sofort
    '''
    screen = turtle.Screen()
    screen.title(title)
    screen.setup(width = width, height = height)
    if listen: screen.listen()
    if tracer is not None: turtle.tracer(tracer)
    return screen

def distance(x,y):
    '''berechnet die Distanz zwischen zwei Punkten x,y
       x und y sind Koordinatenpaare
    '''
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def closest_pt(pt, pts):
    '''pt ist ein Koordinatenpaar, pts eine Liste von Punkten
       gibt den Punkt in pts zurueck, der am naechsten beim Punkt pt liegt
    '''
    res = None
    dist = math.inf
    for p in pts:
        if distance(p,pt) <= dist:
            dist = distance(p,pt)
            res = p
    return res

def nearby(pt, pts, err=10):
    '''gibt True zurueck, falls es in der Liste pts von Punkten einen Punkt gibt,
       dessen Distanz zum Punkt pt kleiner als err ist
    '''
    for p in pts:
        if  distance(p, pt) < err:
            return True


def fly_to(t,x,y):
    """turtle t geht auf Position (x,y) ohne zu zeichnen"""
    isdown = t.isdown()
    t.penup()
    t.goto(x,y)
    if  isdown:
        t.pendown()            

def write(t, pos, text, font = ('Arial', 20), align='center'):
    '''Turtle t schreibt den Text text an der Position pos'''
    fly_to(t, *pos)
    t.write(text, align=align, font=font)
        
def draw_points(t, pts, r=2):
    '''Turtle t zeichnet einen kleinen Kreis bei jedem Punkt in pts'''
    for pt in pts:
        fly_to(t,*pt)
        t.circle(r)

def draw_square_from(t, pos, slen):
    '''turtle t zeichnet ein Quadrat mit der linken unteren Ecke bei pos
       und Seitenlaenge slen
    '''
    fly_to(t, *pos)
    t.setheading(0) 
    for i in range(4):
        t.forward(slen)
        t.left(90) 

def connect_points(t,pts):
    '''turtle t verbidet die Punkte in pts'''
    fly_to(t, *pts[0])
    for pt in pts:
        t.goto(pt)        

def get_turtles(n,hide=True):
    '''get a list of n turtles'''
    tl = [turtle.Turtle() for _ in range(n)]
    for t in tl: t.hideturtle()
    return tl
    
# wird in mTurtle gebraucht
def custom_turtle(t, size=(2,2), shape='circle', angle=0,\
               color=('black','black'), \
               speed=0, pendown=False, pos=(0,0), hide=False, **kwargs):

    t.shape(shape)
    t.turtlesize(*size)
    t.speed(speed)

    if type(color) == tuple and len(color) ==2: t.color(*color)
    else: t.color(color)
    t.left(angle)
    t.penup()
    t.goto(*pos)
    if  pendown:
        t.pendown()
    if  hide:
        t.hideturtle()

    return t        