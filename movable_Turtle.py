
import math
import turtle
import turtle_helpers as th

class movableTurtle(turtle.Turtle):
    '''movable Turtle Class
       methods:
        - start()
        - stop()
        - remove(delete=True)
        - dist()

       class methods:
        - update(screen, delay)    
    
    '''
    tracker = [] # stores dTurtles if no storage is provided
    
    def __init__(self, tracker=None, running = True, maxdist=0, **kwargs):
        '''movable turtle class'''
        super().__init__()

        if  tracker is None:
            self.tracker = movableTurtle.tracker                
        else:
            self.tracker = tracker 

        self.tracker.append(self)
        
        th.custom_turtle(self, **kwargs)
        self.pos0 = self.pos()
        self.maxdist = maxdist
        self.actions = []
        self.action_counter = {}
        self.running = running
      
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
        self.action_counter[f] = 0
    def out_of_screen(self):
        w = self.getscreen().window_width()
        h = self.getscreen().window_height()
        x,y = self.pos()
        if  abs(x) > w//2 or abs(y) > h//2:
            self.remove()

    def out_of_box(self):
        if  self.maxdist > 0 and self.dist() > self.maxdist: 
            self.remove()

    def remove(self,delete=True):
        if  self not in self.tracker:
            return False
        #self.stop()
        self.hideturtle()
        if delete: self.clear()
        self.tracker.remove(self)
    
    def track(self, track=True):
        if  track is False and self  in self.tracker:
            self.tracker.remove(self)
        elif track and self not in self.tracker:
            self.tracker.append(self)
            self.showturtle()

    def is_tracked(self):
        return self in self.tracker

    def action(self):
        if  self.running and self.actions:
            for f in self.actions: 
                f()
                self.action_counter[f] +=1
            if self.maxdist: self.out_of_box()
            else: self.out_of_screen()

    @classmethod
    def update(cls, screen, delay=100):   
        def update_():
            for t in cls.tracker:
                t.action()
            turtle.ontimer(update_, delay)
            screen.update() 

        update_() 

