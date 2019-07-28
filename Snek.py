#Snek Object
from tkinter import *
from tkinter import ttk

class Snek ():
    def __init__(self, master):
        currentDirection = "up"
        x = 320
        y = 440
        canvas = Canvas(master)
        canvas.pack()
        print('created master')

        canvas.config(width = 640, height = 480)
        snek = canvas.create_line(x, y, x, y+30, fill = 'green', width = 15)
        print ('created snek')
    
    

        
#    def getCurrentLocation():{
#       return currentLocation
#      }
'''    
    def turn (way):{
        switch currentLocation{
            case "w":
                if (curentDirection.equals("left")||currentDirection.equals("right")):
                    currentDirection = "up"
                break
            case "s":
                if (curentDirection.equals("left")||currentDirection.equals("right")):
                    currentDirection = "down"
                break
            case "a":
                if (curentDirection.equals("up")||currentDirection.eq("down")):
                    currentDirection = "left"
                break
            case "d":
                if (curentDirection.equals("up")|| currentDirection.equals("down")):
                    currentDirection = "right"
                break
        }
    } 
            

    def go ():{
        if () {
            }
        #check if current location is an edge           
        #update currentLocation
        #call gui function
        #increment appropriate tuple coordinate, draw as head
        #pop off
        } 

    def eat ():{
        #undraw dot
        #increment body by 1 square
        }
'''
        
