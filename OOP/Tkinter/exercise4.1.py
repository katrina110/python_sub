#LEX 6.0 - Exercise 4.1
#Programmed by: Katrina Ricci Batin BSCPE 1-2

import tkinter as tk

def draw_square(event):
    #Get the x and y coordinates of the mouse click event 
    x = event.x
    y = event.y

    # Set the size of the square 
    size = 50

    # Calculate the coordinates of the square
    x1 = x	# x-coordinate of the top-left corner of the square 
    y1 = y	# y-coordinate of the top-left corner of the square
    x2 = x + size	# x-coordinate of the bottom-right corner of the square
    y2 = y + size	# y-coordinate of the bottom-right corner of the square


    # Draw the square on the canvas with a red fill color 
    canvas.create_rectangle(x1, y1, x2, y2, fill="red")

root = tk.Tk() 
root.title("Draw Square") 
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400) 
canvas.pack()

# Bind the mouse click event to the draw_square function 
canvas.bind("<Button-1>", draw_square)

root.mainloop()