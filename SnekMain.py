#Amina Shikhalieva
#Snek is my rendition of the classic game of snake, where a snake eats and
#it grows but cannot run into itself

from tkinter import *
from tkinter import ttk


class SnekMain:
    def __init__(self, master):
            self.label = ttk.Label(master, text = "Snek")
            self.label.grid(row = 0, column = 3, columnspan = 2)
        
    def newDot():{
        #generates rand tuple (0-100,0-100) and draws dot there
        #checks if it's not on snek
        #updates dotLocation
        }
   
    def over ():{
        #player lost, score, high score
        #play again?
        }
    
    end = False
    snek = Snek()
    newDot()

    while (not end):
        wait(5)
        snek.go()
        if (dotLocation.equals(snek.getCurrentLocation)):
            snek.eat()
            newDot()
        #read from keyboard
        snek.turn()
        
def main():
    root = Tk()
    game =  SnekMain(root)
    root.mainloop()

if __name__ == "__main__": main()
