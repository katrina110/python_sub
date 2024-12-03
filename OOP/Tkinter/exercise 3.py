#LEX 6.0 - Exercise 3.1
#Programmed by: Katrina Ricci Batin BSCPE 1-2

from tkinter import * 
import random

app = Tk() 
app.title("Layout Example") 
app.geometry('400x200')

leftFrame = Frame(app, bd=5, relief=GROOVE) 
rightFrame = Frame(app, bd=5, relief=GROOVE) 
leftFrame.pack(side='left', fill=BOTH, expand=1) 
rightFrame.pack(side='right', fill=BOTH, expand=1)

labelA = Label(leftFrame, text="A", bg='blue', width=12) 
labelB = Label(leftFrame, text="B", bg='white', width=12) 
labelC = Label(rightFrame, text="C", bg='white', width=12) 
labelD = Label(rightFrame, text="D", bg='blue', width=12)

labelA.pack(side='top', fill=BOTH, expand=1) 
labelB.pack(side='bottom', fill=BOTH, expand=1) 
labelC.pack(side='top', fill=BOTH, expand=1) 
labelD.pack(side='bottom', fill=BOTH, expand=1)

app.mainloop()