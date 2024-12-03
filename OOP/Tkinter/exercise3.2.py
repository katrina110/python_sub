#LEX 6.0 - Exercise 3.2
#Programmed by: Katrina Ricci Batin 1-2

from tkinter import * 
import random

app = Tk()

app.title("Resizable Layout Example")

# Create two frames and lay them out beside each other 
leftFrame = Frame(app, bd=5, relief=GROOVE)  
rightFrame = Frame(app, bd=5, relief=GROOVE) 
leftFrame.pack(side='left', fill=BOTH, expand=True)
rightFrame.pack(side='right', fill=BOTH, expand=True)

# Create labels inside the frames
labelA = Label(leftFrame, text="A", bg='blue', width=12) 
labelB = Label(leftFrame, text="B", bg='white', width=12) 
labelC = Label(rightFrame, text="C", bg='white', width=12) 
labelD = Label(rightFrame, text="D", bg='blue', width=12)

# Pack labels with expand and fill options to make them grow and expand 
labelA.pack(side='top', fill=BOTH, expand=True) 
labelB.pack(side='bottom', fill=BOTH, expand=True) 
labelC.pack(side='top', fill=BOTH, expand=True) 
labelD.pack(side='bottom', fill=BOTH, expand=True)

app.mainloop()

