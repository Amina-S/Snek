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
    length = 3
    direction = "up"
    segSet = {(x, y)}
    def __init__(self, canvas):
        Snek.canvas = canvas
        canvas.config(width = 640, height = 480)
        Snek.head = segment(canvas, Snek.x, Snek.y, Snek.segSize/2)                                 
        Snek.tail = segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2,
                            segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2, Snek.head))
        Snek.segSet.add((Snek.x, Snek.y))
        Snek.segSet.add((Snek.x, Snek.y+2*Snek.segSize))
        Snek.segSet.add((Snek.x, Snek.y+Snek.segSize))
        #Snek.y = Snek.y-2*Snek.segSize
            
        
##        seg2 = segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2)
##        Snek.tail = segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2)     
##    def turn (way):
##        switch currentLocation{
##            case "w":
##                if (curentDirection.equals("left")||currentDirection.equals("right")):
##                    currentDirection = "up"
##                break
##            case "s":
##                if (curentDirection.equals("left")||currentDirection.equals("right")):
##                    currentDirection = "down"
##                break
##            case "a":
##                if (curentDirection.equals("up")||currentDirection.eq("down")):
##                    currentDirection = "left"
##                break
##            case "d":
##                if (curentDirection.equals("up")|| currentDirection.equals("down")):
##                    currentDirection = "right"
##                break
##        }          
    def attemptMove (self):
        if (Snek.direction == 'up'):
            Snek.y -= Snek.segSize     
        elif (Snek.direction == 'down'):
            Snek.y += Snek.segSize
        elif (Snek.direction == 'left'):
            Snek.x -= Snek.segSize
        else:
            Snek.x += Snek.segSize
            
        print ('in attemptmove(), new x is ', Snek.x, 'new y is ', Snek.y, '\n')                     #complicated bc centers of segnemts don't perfectly overlap
        print('segSet:')
        for i in Snek.segSet:
            print(i)
            
        if (Snek.x<Snek.segSize or Snek.x>640-Snek.segSize or Snek.y<Snek.segSize or Snek.y>480-Snek.segSize):
            print('returning false bc boundary check')
            return False
        if ((Snek.x, Snek.y) in Snek.segSet):
            print('returning false because x,y in segSet')
            return False
        Snek.segSet.add((Snek.x, Snek.y))              
        new = segment(Snek.canvas, Snek.x, Snek.y, Snek.segSize/2)
        Snek.tail.deleteSeg(Snek.canvas)
        Snek.segSet.discard((Snek.x, Snek.y))    
        Snek.tail = new
        return True
        
##    def eat ():
##        #undraw dot



    
