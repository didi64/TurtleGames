
import math
import ID
import turtle
import turtle_helpers as th

class movableTurtle(turtle.Turtle):
    store = [] # stores dTurtles if no storage is provided
    
    def __init__(self, name=None, store=None, running = True, maxdist=0, **kwargs):
        '''movable turtle class'''
        super().__init__()
        self.name=name
        if  store is None:
            self.store = movableTurtle.store                
        else:
            self.store = store 
        self.store.append(self)
        
        th.custom_turtle(self, **kwargs)
        self.name = 'mT' + str(ID.new_id()) if name is None else name
        self.pos0 = self.pos()
        self.maxdist = maxdist
        self.actions = []
        self.running = running
      
    def __repr__(self): return self.name

    def dist(self):
       x,y= self.pos()
       x0,y0 = self.pos0
       return math.sqrt((x-x0)**2 + (y-y0)**2)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def add_action(self,f):
        self.actions.append(f)

    def out_of_screen(self):
        w,h = self.getscreen().screensize() 
        x,y = self.pos()
        if  abs(x) > w//2 or abs(y) > h//2:
            self.remove()

    def out_of_box(self):
        if  self.dist() > self.maxdist: 
            self.remove()

    def remove(self):
        self.stop()
        self.hideturtle()
        self.clear()
        self.store.remove(self)

    def action(self):
        if  self.running and self.actions:
            for f in self.actions: 
                f()
            if self.maxdist: self.out_of_box()
            else: self.out_of_screen()

    @classmethod
    def update(cls, screen, delay=100):   
        def update_():
            for t in cls.store:
                t.action()
            turtle.ontimer(update_, delay)
            screen.update() 

        update_() 

