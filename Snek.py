from tkinter import *
from tkinter import ttk

class Snek ():
    x = 320
    y = 420
    
    def __init__(self, master):
        currentDirection = "up"
        canvas = Canvas(master)
        canvas.pack()
        canvas.config(width = 640, height = 480)
        snek = canvas.create_line(self.x, self.y, self.x, self.y+60, fill = 'green', width = 16)

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
        if (self.x<8 or self.x>320-8 or self.y<0 or self.y>420):
            return False

        #draw new nodes
        return True
        
##    def eat ():
##        #undraw dot
##        #increment body by 1 square
    
