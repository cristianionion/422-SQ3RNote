# Importing tkinter module
from tkinter import *
from tkinter import messagebox, filedialog
import os

def createWidgets():
    new = Toplevel(root)
    new.geometry("800x800")
    new.title("Untitled - Note")
    global textArea
    textArea = Text(new)
    textArea.grid(sticky=N+E+S+W)

    menuBar = Menu(new)
    new.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command="")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command="")
    menuBar.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command="")
    editMenu.add_command(label="Copy", command="")
    editMenu.add_command(label="Paste", command="")
    menuBar.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Noepad", command="")
    menuBar.add_cascade(label="Help", menu=helpMenu)

def newFile():
    global textArea
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global textArea
    file=filedialog.askopenfile(defaultextension=".txt", filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    file = file.name

    if file =="":
        file = None
    else:
        root.title(os.path.basename((file) + " - Notepad"))
        textArea.delete(1.0, END)
        file = open(file, "rb")
        textArea.insert(1.0, file.read())
        file.close()

def saveFile():


# Creating a tkinter window
root = Tk()

# Initialize tkinter window
# with dimensions 300 x 250
root.geometry('800x800')

# Creating a Button
btn1 = Button(root, fg="blue", text='New Book', height=10, width=20,
              command=createWidgets)
btn1.grid(row=0, column=0)

root.mainloop()