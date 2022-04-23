from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
import os


def book_Menu():

    global root
    root = tk.Tk()

    # Initialize tkinter window
    # with dimensions 300 x 250
    root.geometry('800x800')

    # Creating a Button
    btn1 = Button(root, fg="blue", text='New Book', height=10, width=20,
                  command=book_Input)

    btn1.grid(row=0, column=0)

    root.mainloop()

def book_name():
   global book_title
   string= entry.get()
   book_title = string
   if book_title != None:
      small.destroy()
      chapter_Menu()


def book_Input():
   global small
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="", font=("Courier 22 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()
   tk.Button(small, text="Okay", width=20, command=book_name).pack(pady=20)

def chapter_Menu():
    global chptrMenu
    chptrMenu = Toplevel(root)
    chptrMenu.geometry("800x800")
    chptrMenu.title(book_title)
    chptrbtn = Button(chptrMenu, fg="blue", text='New Chapter', height=10, width=20,
                      command=chapter_Input)

    chptrbtn.grid(row=0, column=0)

def chapter_Menu_add_button():
    global chapter_counter
    if chapter_title != None:
        chapter_name = chapter_title
        newbtn = Button(chptrMenu, fg="blue", text=chapter_name, height=10, width=20,
                        command=lambda: openFile(chapter_name))
        chapter_counter += 1
        newbtn.grid(row=0, column=chapter_counter)
    pass

def chapter_name():
   global chapter_title
   string= entry.get()
   chapter_title = string
   chapter_dict[chapter_title] = None
   if chapter_title != None:
      small.destroy()

      Text_Editor()


def chapter_Input():
   global small
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="", font=("Courier 22 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()



   # Create a Button to validate Entry Widget
   tk.Button(small, text="Okay", width=20, command=chapter_name).pack(pady=20)



def Text_Editor():
    #text_editor = Text(root)
    #text_editor.pack()
    #text_editor.mainloop()

    #new = Toplevel(root)
    #new.geometry("800x800")
    #new.title("Untitled - Note")
    global textArea
    global questArea
    global new




    new = Toplevel(root)
    textFrame = Frame(new,width=300, height=400)
    questFrame = Frame(new, width=300, height=100)
    textArea = tk.Text(textFrame)
    questArea = tk.Text(questFrame)




    btnFrame = tk.Frame(new)
    prmptFrame = tk.Frame(new)

    btnSave = tk.Button(btnFrame, text = "save", command=saveFile)
    btnChptr = tk.Button(btnFrame, text = "new chapter", command=chapter_Input)
    btnPrompt = tk.Button(prmptFrame, text = "Toggle SQ3R", command="")

    #textArea.grid(sticky= N + E + S + W)
    #questArea.grid(sticky=N + E + S + W)

    # creates scroll bar
    #ScrollBar = Scrollbar(textArea)

    new.title(book_title + "-" + chapter_title)

    new.protocol("WM_DELETE_WINDOW", on_closing)

    menuBar = Menu(new)
    new.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command="")
    menuBar.add_cascade(label="File", menu=fileMenu)





    # makes text box horizontally resizable (do we want this?)
    #root.grid_rowconfigure(0, weight=1)
    new.grid_columnconfigure(0, weight=1)

    # places button on grid:
    #   "ew" : forces buttons to expand horizontally
    #   padx/pady : horizontal/vertical padding given to button
    btnSave.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btnChptr.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btnPrompt.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

    textArea.grid(row=0, column=1, sticky="nsew")
    questArea.grid(row=1, column=1, sticky="nsew")

    # creates grid, with distinct columns for btns and text editor
    textFrame.grid(row=0, column=1, sticky="nsew")
    questFrame.grid(row=1, column=1)
    btnFrame.grid(row=0, column=0, sticky="ns")
    prmptFrame.grid(row=0, column=3, sticky="ns")



    # implements scroll bar
    #ScrollBar.pack(side=RIGHT, fill=Y)
    #ScrollBar.config(command=textArea.yview)
    #textArea.config(yscrollcommand=ScrollBar.set)






def saveFile():
    '''
    saveas = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                      defaultextension=".txt",
                                      filetypes = [("All Files", "*.*"),
                                                    ("Test Documents", "*.txt")])
    '''

    chapter_dict[chapter_title] = (textArea.get(1.0,END), questArea.get(1.0,END))
    book_dict[book_title] = chapter_dict

    chapter_Menu_add_button()

    print(book_dict[book_title][chapter_title][0])
    print(book_dict[book_title][chapter_title][1])




    '''
    if saveas != None:

        file = open(saveas, "w")
        file.write(textArea.get(1.0, END))
        file.close()

        root.title(os.path.basename(saveas))
    pass
    '''

def newFile():
    global textArea
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile(chapter_name):
    global textArea


    try:
        textArea.delete(1.0, END)
        questArea.delete(1.0, END)
    except:
        Text_Editor()
        pass




    notes = chapter_dict[chapter_name][0]
    questions = chapter_dict[chapter_name][1]
    textArea.insert("1.0", notes)
    questArea.insert("1.0", questions)

    pass

    '''
    file = filedialog.askopenfile(defaultextension=".txt",
                                  filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])


    if file == None:
        pass
    else:
        file = file.name
        root.title(os.path.basename((file) + " - Notepad"))
        textArea.delete(1.0, END)
        file = open(file, "rb")
        textArea.insert(1.0, file.read())
        file.close()
    '''

def create():
   pass

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit without saving?"):

        new.destroy()


# these dictionaries need to come from somewhere else (database)
book_dict = {}

chapter_dict = {}

chapter_counter = 0
book_Menu()

