#LEX 6.0 - EXERCISE 1: A First GUI Program
#Programmed by: Katrina Ricci C Batin BSCPE 1-2
from tkinter import *

def clicked():
    print("Button Pressed!")


app = Tk()
app.title("Modified GUI Example") 
app.geometry('400x300')

button1 = Button(app, text="Press Me!", command=clicked) 
button1.pack(side='top')

app.mainloop()