import turtle
import math

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

def screen(title='Test', width=500, height=500, listen=True, tracer=0):   
    ''''set up screen'''
    screen_ = turtle.Screen()
    screen_.title(title)
    screen_.setup(width = width, height = height)
    if listen: screen_.listen()
    if tracer is not None: turtle.tracer(tracer)
    return screen_

def distance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

def closest_pt(pt, pts):
    ''' return point in pts that is closest to pt'''
    res = None
    dist = math.inf
    for p in pts:
        if distance(p,pt) <= dist:
            dist = distance(p,pt)
            res = p
    return res

def nearby(pt, pts, err=10):
    '''check if pt is close to some p in pts'''
    for p in pts:
        if  distance(p, pt) < err:
            return True


def fly_to(t,x,y):
    """turtle t goes to position x,y without drawing"""
    isdown = t.isdown()
    t.penup()
    t.goto(x,y)
    if  isdown:
        t.pendown()            

def write(t, pos, text, font = ('Arial', 20), align='center'):
    fly_to(t, *pos)
    t.write(text, align=align, font=font)
        
def draw_points(t, pts, r=2):
    for pt in pts:
        fly_to(t,*pt)
        t.circle(r)

def draw_square_from(t,pos,slen):
    fly_to(t, *pos)
    t.setheading(0) 
    for i in range(4):
        t.forward(slen)
        t.left(90) 

def connect_points(t,pts):
    fly_to(t, *pts[0])
    for pt in pts:
        t.goto(pt)        