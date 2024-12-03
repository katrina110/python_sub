#LEX 6.0 - Exercise 2.2: Part B: Complete Program 
#Programmed by: Emanuel Jabon BSCPE 1-2

from tkinter import *

# Function to handle button click 
def clicked():
    input_text = entry1.get() 
    print("You entered:", input_text) 
    button1.config(text=input_text)

# Create the main window 
window = Tk()
window.title("Text Input Example") 
window.geometry('300x200')

# Create a frame for the bottom panel 
bottom_panel = Frame(window) 
bottom_panel.pack(side=BOTTOM, padx=10, pady=10)

# Create a label to prompt the user
prompt_label = Label(bottom_panel, text="Enter a word:") 
prompt_label.pack()

# Create a frame for the input panel 
input_panel = Frame(bottom_panel) 

input_panel.pack()

# Create an entry widget for text input
entry1 = Entry(input_panel) 
entry1.pack(side=LEFT)

# Create a button
button1 = Button(bottom_panel, text="Submit", command=clicked) 
button1.pack()

# Start the application
window.mainloop()