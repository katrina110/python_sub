#LEX 6.0 - Exercise 2.3: Elaborations
#Programmed by: Katrina Ricci Batin 1-2

from tkinter import *

def buttonClicked(): 
    inputText = entry.get()

    if len(inputText) == 0: 
        button.config(bg='red')
    else:
        button.config(bg='SystemButtonFace') 
        label.config(text="You entered: " + inputText) 
        entry.delete(0, END)
        button.config(text="Text Copied!")


app = Tk()
app.title("Text Input Example") 
app.geometry('300x200')

labelPrompt = Label(app, text="Enter a word:") 
labelPrompt.pack()

entry = Entry(app) 
entry.pack()

label = Label(app, text="") 
label.pack()

button = Button(app, text="Copy Text", command=buttonClicked) 
button.pack(side='bottom')

app.mainloop()