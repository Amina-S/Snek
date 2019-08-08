from tkinter import *
from tkinter import ttk

class segment():
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
    y = 420
    segSize = 16
    direction = "Up"
    segSet = {(x, y)}
    def __init__(self, canvas):
        Snek.canvas = canvas
        canvas.config(width = 640, height = 480)
        Snek.head = segment(canvas, Snek.x, Snek.y, Snek.segSize/2)
        seg2 = segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2, Snek.head)
        Snek.tail = segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2, seg2)
        Snek.segSet.add((Snek.x, Snek.y))
        Snek.segSet.add((Snek.x, Snek.y+2*Snek.segSize))
        Snek.segSet.add((Snek.x, Snek.y+Snek.segSize))            
          
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
            return False
        if ((Snek.x, Snek.y) in Snek.segSet):
            return False
        Snek.segSet.add((Snek.x, Snek.y))              
        new = segment(Snek.canvas, Snek.x, Snek.y, Snek.segSize/2)
        Snek.head.setPrev(new)
        Snek.head = new
        Snek.tail.deleteSeg(Snek.canvas)
        Snek.segSet.discard((Snek.x, Snek.y))    
        Snek.tail = Snek.tail.prev
        return True
        
##    def eat ():
##        #undraw dot



    
