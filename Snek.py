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
        
class Snek ():
    x = 320
    y = 420
    segSize = 16
    def __init__(self, master):
        currentDirection = "up"
        canvas = Canvas(master)
        canvas.pack()
        canvas.config(width = 640, height = 480)
        seg1 = segment(canvas, Snek.x, Snek.y, Snek.segSize/2)
        seg2 = segment(canvas, Snek.x, Snek.y+Snek.segSize, Snek.segSize/2)
        seg3 = segment(canvas, Snek.x, Snek.y+2*Snek.segSize, Snek.segSize/2)
         

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
        #create new node in current direction
            #if this is a duplicate of another list element, return false
        #remove last node
        if (self.x<segDist or self.x>320-segDist or self.y<segDist or self.y>420-segDist):
            return False

        #draw new nodes
        return True
        
##    def eat ():
##        #undraw dot
##        #increment body by 1 square
    
