#Amina Shikhalieva
#Snek is my rendition of the classic game of snake, where a snake eats and
#grows but cannot run into itself

from tkinter import *
from tkinter import ttk
from Snek import Snek

       
def quitGame():
           exit()
           
class SnekMain ():
     
    
    def __init__(self, mas):
       mas.title("Snek") 
       mas.geometry("500x400")
       #mas.resizeable(False, False)
       mas.l1 = ttk.Label(mas, text = "Snek", font = ('Courier', 28, 'bold'),
                             justify = CENTER, foreground = 'dark green')
       pic = PhotoImage(file = 'C:\\Users\\Home\\Cornell\\CS\\Projects\\Snek\\SnekPic-2.gif') #remember to include this into project files

       
       mas.l1.config (image = pic)
       mas.l1.image = pic
       mas.l1.config (compound = "bottom")
       mas.l1.pack()

       fra1 = ttk.Frame(mas)
       fra1.config(relief = RIDGE, padding = (9,9))
       fra1.pack()
       mas.b1 = ttk.Button (fra1, text = "Begin",padding = (5,5))
       mas.b2 = ttk.Button (fra1, text = 'Instructions',padding = (5,5))
       mas.b3 = ttk.Button (fra1, text = 'Quit',padding = (5,5))
       
       mas.b3.config(command = quitGame)
       
       mas.b1.grid()
       mas.b2.grid()
       mas.b3.grid()
    
                            
        
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
