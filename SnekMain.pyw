#Amina Shikhalieva
#Snek is my rendition of the classic game of snake, where a snake eats and
#grows but cannot run into itself

from tkinter import *
from tkinter import ttk
from Snek import Snek
  
def quitGame():
    exit()

    
def launchGame():
    window = Toplevel (root)
    window.title('Snek')
    root.state('withdrawn')
    window.lift()
    canvas = Canvas(window)
    canvas.pack()
    snek = Snek(canvas)
    #maybe include a countdown sequence here
    #also could listen for esc key to pause game, quit, or restart
    #maybe speed options as well
    #optional dark mode?

    def key(event):
        sym = event.keysym
        if (sym == 'Up' or sym == 'Down' or sym == 'Left' or sym == 'Right'):
            snek.turn(sym)
        elif (sym == 'Escape'):
            #need pause option
            quitGame()
            
    cont = True;
    while (cont):
        cont = snek.attemptMove()
        window.update()
        window.after(150)
        window.bind('<KeyPress>', key)
        Snek.newDot()


def instructions():
    window = Toplevel (root)
    window.title('Instructions')
    window.lift()
    #don't forget to actually write instructions
    
root = Tk()
root.title("Snek") 
root.geometry("500x400")
root.l1 = ttk.Label(root, text = "Snek", font = ('Courier', 28, 'bold'),
                     justify = CENTER, foreground = 'dark green')
pic = PhotoImage(file =
                 'C:\\Users\\Home\\Cornell\\CS\\Projects\\Snek\\SnekPic-2.gif') 

root.l1.config (image = pic)
root.l1.image = pic
root.l1.config (compound = "bottom")
root.l1.pack()

fra1 = ttk.Frame(root)
fra1.config( padding = (9,9))
fra1.pack()
root.b1 = ttk.Button (fra1, text = "Begin",padding = (5,5))
root.b1.config(command = launchGame)
root.b2 = ttk.Button (fra1, text = 'Instructions',padding = (5,5))
root.b2.config(command = instructions)
root.b3 = ttk.Button (fra1, text = 'Quit',padding = (5,5))
root.b3.config(command = quitGame)

root.b1.grid()
root.b2.grid()
root.b3.grid()



def over ():
    #player lost, score, high score
    #play again? if not, quit()
    x=3

root.mainloop()
if __name__ == "__main__": main()
