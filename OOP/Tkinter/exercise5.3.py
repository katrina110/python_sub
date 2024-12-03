#LEX 6.0 - Exercise 5.3
#Programmed by: Katrina Ricci Batin BSCPE 1-2

from tkinter import *
from tkinter import messagebox, filedialog

# Create the main application window 
app = Tk()
app.title("File Changer") 
app.geometry('400x400')

# Variables 
fileName = None 
fileContents = None 
fileChanged = False

# Create handlers for menu items 
def exitApp():
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Exit with unsaved changes?", default=messagebox.NO)
        if ans == "yes": app.destroy()
    else:
        app.destroy()

def giveHelp():
    ans = messagebox.askquestion("Not Much Help", "Are you sure you need help?", default=messagebox.NO)

def aboutMsg():
    messagebox.showinfo("About File Changer", "This application converts a text file to uppercase.")

def openFile():
    global fileName, fileContents, fileChanged 
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Discard changes and open a new file?", default=messagebox.NO)
        if ans == "no": 
            return
    filename = filedialog.askopenfilename(title="Choose a file to open", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename: 
        try:
            with open(filename, 'r') as file: 
                fileContents = file.read()
            fileName = filename 
            fileChanged = False
        except:
            messagebox.showerror("File Error", "Failed to open the file.")

def saveFile():
    global fileName, fileContents, fileChanged 
    if not fileName:
        messagebox.showerror("No File", "No file open.") 
        return
    if not fileChanged:
        messagebox.showinfo("No Changes", "The file has not changed.")

    return
try:

        with open(fileName, 'w') as file: 
            file.write(fileContents)
        fileChanged = False
        messagebox.showinfo("File Saved", "File successfully saved.")

except:
        messagebox.showerror("File Error", "Failed to save the file.")

def upperCmd():
    global fileContents, fileChanged 
    if not fileName:
        messagebox.showerror("No File", "No file open.")
        return
    if fileChanged:
        ans = messagebox.askquestion("Unsaved Changes", "Discard changes and convert to uppercase?", default=messagebox.NO)
        if ans == "no":
            return
    fileContents = fileContents.upper() 
    fileChanged = True

# Create menu bar and menus 
menuBar = Menu(app) 
app.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0) 
fileMenu.add_command(label='Open', command=openFile) 
fileMenu.add_command(label='Save', command=saveFile) 
fileMenu.add_command(label='Quit', command=exitApp) 
menuBar.add_cascade(label='File', menu=fileMenu)

editMenu = Menu(menuBar, tearoff=0) 
editMenu.add_command(label='Convert to Uppercase', command=upperCmd) 
menuBar.add_cascade(label='Edit', menu=editMenu)

helpMenu = Menu(menuBar, tearoff=0) 
helpMenu.add_command(label='Help', command=giveHelp) 
helpMenu.add_command(label='About', command=aboutMsg)
menuBar.add_cascade(label='Help', menu=helpMenu)

app.mainloop()