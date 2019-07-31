from tkinter import *
from tkinter import ttk

class segment():
    def __init__(self, can, x, y, dist, nextNode = None):
        self.x = x
        self.y = y
        self.dist = dist
        self.can = can
        self.nextNode = nextNode
        square = can.create_rectangle(x-dist, y-dist, x+dist, y+dist)
        can.itemconfigure(square, fill = 'dark green')
    def setNext(self, node):
        self.nextNode = node
        
class Snek ():
    x = 320
    y = 420
    segSize = 16
    
    def __init__(self, master):
        self.direction = "up"
        canvas = Canvas(master)
        canvas.pack()
        canvas.config(width = 640, height = 480)
        self.head = segment(canvas, Snek.x, Snek.y, Snek.segSize/2)
        seg2 = segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2)
        self.tail = segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2)
        self.length = 3

#    def getCurrentLocation():
#       return currentLocation

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
        dist =  self.segSize/2
        if (self.x<dist or self.x>640-dist or self.y<dist or self.y>480-dist):
            return False
        #create new node in current direction
        if (self.direction == 'up'):
            self.x += self.segSize
        elif (self.direction == 'down'):
            self.x -= self.segSize
        elif (self.direction == 'left'):
            self.y -= self.segSize
        else:
            self.y += self.segSize
        #if this is a duplicate of another list element, return false
        for i in range(self.length):
            
        new = segment(canvas, self.x, self.y, dist)
        self.tail.setNext(new)
        self.tail = new
        self.length++
        
        
        
        return True
        
##    def eat ():
##        #undraw dot
##        #increment body by 1 square
    
