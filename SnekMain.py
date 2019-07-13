#Amina Shikhalieva
#Snek is my rendition of the classic game of snake, where a snake eats and
#grows but cannot run into itself

from tkinter import *
from tkinter import ttk
from Snek import Snek


        
def newDot():{
            #generates rand tuple (0-100,0-100) and draws dot there
            #checks if it's not on snek
            #updates dotLocation
            }
   
def over ():{
        #player lost, score, high score
        #play again?
        }

class SnekMain:
    def __init__(self, master):
     #   self.title("Snek") 
        self.geometry("500x500")
        self.text = ttk.Text(master, text = "Snek")
        self.text.grid(row = 0, column = 3, columnspan = 2)
    end = False
    snek = Snek()
    newDot()
    '''
    while (not end):
        wait(5)
        snek.go()
        if (dotLocation.equals(snek.getCurrentLocation)):
            snek.eat()
            newDot()
        #read from keyboard
        snek.turn()
        '''
        
def main():
    root = Tk()
    game =  SnekMain(root)s
    root.mainloop()

if __name__ == "__main__": main()
