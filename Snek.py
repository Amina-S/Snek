from tkinter import *
from tkinter import ttk
from random import randrange

class Dot():
    def __init__(self, can, x, y):
        self.x = x
        self.y = y
        x1, x2 = x-2, x+2
        y1, y2 = y-2, y+2
        self. point = can.create_oval(x1, y1, x2, y2, fill = 'blue')
    def eatDot (self, can):
        can.delete(self.point)
    
    
class Segment():
    def __init__(self, can, x, y, dist, prev = None):
        self.x = x
        self.y = y
        self.dist = dist
        self.can = can
        self.prev = prev
        self.square = can.create_rectangle(x-dist, y-dist, x+dist, y+dist)
        can.itemconfigure(self.square, fill = 'dark green')
    def setPrev(self, node):
        self.prev = node
    def deleteSeg(self, can):
        can.delete(self.square)
   
class Snek ():
    x = 320
    y = 400
    segSize = 16
    direction = "Up"
    segSet = set([]) 

    def newDot():
        dotx= randrange(Snek.segSize, 640 - Snek.segSize + 1, Snek.segSize)
        doty = randrange(Snek.segSize, 480 - Snek.segSize + 1, Snek.segSize)
        while ((dotx, doty) in Snek.segSet): 
            dotx = randrange(Snek.segSize, 640 - Snek.segSize + 1, Snek.segSize)
            doty = randrange(Snek.segSize, 480 - Snek.segSize + 1, Snek.segSize)
        return (dotx, doty)
    
    def __init__(self, canvas):
        Snek.canvas = canvas
        canvas.config(width = 640, height = 480)
        Snek.head = Segment(canvas, Snek.x, Snek.y, Snek.segSize/2)
        seg2 = Segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2, Snek.head)
        Snek.tail = Segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2, seg2)
        Snek.currentDot = Dot(canvas, *Snek.newDot())
          
    def turn (self, way):
        if (way == 'Up' or way == 'Down'):
            if (Snek.direction == 'Left' or Snek.direction == 'Right'):
                Snek.direction = way
        if (way == 'Left' or way == 'Right'):
            if (Snek.direction == 'Up' or Snek.direction == 'Down'):
                Snek.direction = way        
        
    def attemptMove (self):
        if (Snek.direction == 'Up'):
            Snek.y -= Snek.segSize     
        elif (Snek.direction == 'Down'):
            Snek.y += Snek.segSize
        elif (Snek.direction == 'Left'):
            Snek.x -= Snek.segSize
        else:
            Snek.x += Snek.segSize            
        if (Snek.x<Snek.segSize or Snek.x>640-Snek.segSize or Snek.y<Snek.segSize or Snek.y>480-Snek.segSize):
            print('stopped because bouds error, x: ',Snek.x,' y: ',Snek.y)
            return False            
        if ((Snek.x, Snek.y) in Snek.segSet): 
            print('stopped because new seg in segSet')
            print ('segSet:')
            for i in Snek.segSet:
                print (i)
            print ('x: ',Snek.x,' y: ',Snek.y)
            return False
        Snek.segSet.add((Snek.x, Snek.y))
        new = Segment(Snek.canvas, Snek.x, Snek.y, Snek.segSize/2)
        Snek.head.setPrev(new)
        Snek.head = new
        if ((Snek.x, Snek.y) != (Snek.currentDot.x, Snek.currentDot.y)):
            Snek.tail.deleteSeg(Snek.canvas)
            Snek.segSet.discard((Snek.tail.x, Snek.tail.y)) 
            Snek.tail = Snek.tail.prev
        else:
            Dot.eatDot(Snek.currentDot, Snek.canvas)
            Snek.currentDot = Dot(Snek.canvas, *Snek.newDot())
        return True

    
      




    
