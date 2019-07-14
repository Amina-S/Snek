#Amina Shikhalieva
#Snek is my rendition of the classic game of snake, where a snake eats and
#grows but cannot run into itself

from tkinter import *
from tkinter import ttk
from Snek import Snek

        

class SnekMain ():
    def __init__(self, master):
       master.title("Snek") 
       master.geometry("1000x600")
       
       master.l1 = ttk.Label(master, text = "Snek", anchor = "center", font = "Calibri")
       master.l1.pack()
        
    end = False
    snek = Snek()
  #  newDot()
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
    def newDot():
            #generates rand tuple (0-100,0-100) and draws dot there
            #checks if it's not on snek
            #updates dotLocation
          x = 2  
   
    def over ():
        #player lost, score, high score
        #play again?
        x=3

        
def main():
    root = Tk()

    game =  SnekMain(root)
    root.mainloop()
    
if __name__ == "__main__": main()
