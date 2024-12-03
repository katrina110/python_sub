#LEX 6.0 - Exercise 2.1: Part A: Getting and Setting Attributes 
#Programmed by: Katrina Ricci C. Batin BSCPE 1-2

from tkinter import *

# Create the main window
window = Tk()
window.title("Label and Button Example") 
window.geometry('200x100')

# Function to change the label text
def changeLabelText():
    if label_text['text'] == "Open": 
        label_text['text'] = "Close"
    else:
        label_text['text'] = "Open"

# Create a button
button_change = Button(window, text="Change Text", command=changeLabelText)

# Create a label
label_text = Label(window, text="Open")

# Place the button and label in the window 
label_text.pack(side='bottom') 
button_change.pack(side='bottom')

# Start the application 
window.mainloop()
