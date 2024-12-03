#LEX 6.0 - Exercise 5.2
#Programmed by: Katrina Ricci Batin BSCPE 1-2

from tkinter import *
from tkinter import messagebox, filedialog

def exitApp():
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Exit with unsaved changes?", default=messagebox.NO)
        if ans == "yes": 
            app.destroy()
    else:
        app.destroy()

def giveHelp():
    ans = messagebox.askquestion("Not Much Help", "Are you sure you need help", default=messagebox.NO)

def aboutMsg():
    messagebox.showinfo("About Exercise 6", "Application to change text file to uppercase")

def openFile():
    global fileName, fileContents, fileChanged 
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Overwrite unsaved changes?", default=messagebox.NO)
        if ans == "no": 
            return
    fileName = filedialog.askopenfilename(title="Choose a file to open", filetypes=[("Text", ".txt"), ("All Files", ".*")])
    if fileName:
        with open(fileName, 'r') as file: fileContents = file.read()
fileChanged = False

def saveFile():
    global fileName, fileContents, fileChanged 
    if not fileName:
        messagebox.showerror("No file", "No file open") 
        return
    if not fileChanged:
        messagebox.showinfo("No changes", "File has not changed") 
        return
    with open(fileName, 'w') as file: 
        file.write(fileContents)
    fileChanged = False
    messagebox.showinfo("File written", "File updated")

def upperCmd():
    global fileContents, fileChanged 
    if not fileName:
        messagebox.showerror("No file", "No file open") 
        return
    fileContents = fileContents.upper() 
    fileChanged = True

app = Tk() 
app.title("File Changer") 
app.geometry('400x400')

fileName = None 
fileContents = None 
fileChanged = False

menuBar = Menu(app) 
app.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0) 
fileMenu.add_command(label='Open', command=openFile) 
fileMenu.add_command(label='Save', command=saveFile) 
fileMenu.add_command(label='Quit', command=exitApp) 
menuBar.add_cascade(label='File', menu=fileMenu)

editMenu = Menu(menuBar, tearoff=0) 
editMenu.add_command(label='Convert to Upper', command=upperCmd) 
menuBar.add_cascade(label='Edit', menu=editMenu)

helpMenu = Menu(menuBar, tearoff=0) 
helpMenu.add_command(label='Help', command=giveHelp) 
helpMenu.add_command(label='About', command=aboutMsg) 
menuBar.add_cascade(label='Help', menu=helpMenu)

app.mainloop()