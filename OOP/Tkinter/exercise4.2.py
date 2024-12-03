#LEX 6.0 - Exercise 4.2
#Programmed by: Katrina Ricci Batin BSCPE 1-2

from tkinter import *
app = Tk()	# Create the top-level window 
app.title("GUI Example 5")	# OPTIONALLY set the title 
app.geometry('400x400')	# OPTIONALLY set the size

# Create a canvas
#  	
#	- background is blue (this is a bit odd) 
#	- make it as large as the main window 
canvas = Canvas(app, bg='blue') 
canvas.pack(expand=1, fill=BOTH)

# Event bindings 
# 
#	Bind mouse or key press events to functions

# Handler for the SHAPE key press event

#	 
shape = "s"

def sKey(event): 
    global shape
    print("Now drawing squares") 
    shape = "s"

def cKey(event): 
    global shape
    print("Now drawing circles") 
    shape = "c"

app.bind("<KeyPress-s>", sKey) 
app.bind("<KeyPress-c>", cKey)

# Handler for the FILL key press event 
#	 
fill = False

def fKey(event): 
    global fill
    print("Now drawing unfilled shapes") 
    fill = False

def FKey(event): 
    global fill
    print("Now drawing filled shapes") 
    fill = True

app.bind("<KeyPress-f>", fKey) 
app.bind("<KeyPress-F>", FKey)

# Handler for the COLOUR key press event 
#	 
colour = "yellow"

def rKey(event): 
    global colour
    print("Now drawing in red") 
    colour = "red"

def yKey(event): 
    global colour
    print("Now drawing in yellow") 
    colour = "yellow"

app.bind("<KeyPress-r>", rKey) 
app.bind("<KeyPress-y>", yKey)

# Handler for a mouse click event 
# 	 
#Draw shape at mouse click
#
# Size is fixed 
X = 50
Y = 50

def mouseClick(event): 
    mx = event.x
    my = event.y
    if shape == "s": 
        if fill:
            canvas.create_rectangle(mx, my, mx + X, my + Y, width=5, outline=colour, fill=colour)
        else:
            canvas.create_rectangle(mx, my, mx + X, my + Y, width=5, outline=colour)
    else:
        if fill:
            canvas.create_oval(mx, my, mx + X, my + Y, width=5, outline=colour, fill=colour)
        else:
            canvas.create_oval(mx, my, mx + X, my + Y, width=5, outline=colour)

canvas.bind("<Button-1>", mouseClick)

app.mainloop()	# Start the main loop