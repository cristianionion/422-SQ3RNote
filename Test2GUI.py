from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
import os
from main import *


def book_Menu():
    # root: the root of our tkinter windows
    global book_dict
    global chapter_dict
    global chapter_counter
    global book_row_counter
    global book_column_counter
    global chapter_row_counter
    global chapter_column_counter
    global prompt_list
    global prmptBool
    global blockBool
    blockBool = False
    prmptBool = True
    prompt_list = [
        "Survey: Scan the text and pay attention to headings, section titles, pictures and graphs to get the big idea.\n",
        "Question: Ask yourself some questions that you’d like to know the answer to after reading the text.\n",
        "Read: Read the text and take note of your readings. Try to find answers to your questions.\n",
        "Recite: Repeat important parts or a summary of what you have read.\n",
        "Review: Look back on your notes and try to review the idea of the text you’ve read.\n"]

    book_column_counter = 1
    chapter_row_counter = 0

    chapter_column_counter = 1
    book_row_counter = 0

    book_dict = db_convert_to_dictionary()
    chapter_dict = {}
    chapter_counter = 0

    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", menu_close)

    # book_counter: keeps track of how many books need to be in the menu
    global book_counter
    book_counter = 0

    # Initialize tkinter window
    # with dimensions 300 x 250
    root.geometry('800x800')

    for i in range(4):
        root.columnconfigure(i, weight=5, minsize=50)
        root.rowconfigure(i, weight=5, minsize=50)

    # creates a 'New Book' Button
    btn1 = Button(root, fg="blue", text='New Book', height=10, width=20,
                  command=book_Input)

    btn1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    # book_list: list of all book keys (titles)
    book_list = book_dict.keys()
    print(book_list)

    # goes thru book_list, creating a button for every book title
    for item in book_list:

        if item != None:
            book_Menu_add_button(item)

    # places btn1


    # keeps window(s)up
    root.mainloop()

def promptToggle():
    global prmptFrame
    global prmptBool
    global labelPrompt
    if prmptBool:
        prompt = prompt_list[0] + prompt_list[1] + prompt_list[2] + prompt_list[3] + prompt_list[4]
        labelPrompt = tk.Label(prmptFrame, text=prompt)
        labelPrompt.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        prmptBool = False
    else:
        labelPrompt.destroy()
        prmptBool = True


def questToggle():
    global new
    global blockFrame
    global blockBool
    if blockBool:
        blockFrame.destroy()
        blockBool=False
    else:
        blockFrame = Frame(new, width=300, height=400, bg="black")
        blockFrame.grid(row=0, column=1, sticky="nsew")
        blockBool=True
    pass


def book_Menu_add_button(book_title):
    global book_counter
    global book_row_counter
    global book_column_counter

    print("book_Menu_add_button:", book_title)
    chapters = book_dict[book_title]

    newbtn = Button(root, fg="blue", text=book_title, height=10, width=20,
                    command=lambda: openBook(chapters, book_title))

    book_counter += 1
    if (book_counter % 5) == 0:
        book_row_counter += 1
        book_column_counter = 0

    newbtn.grid(row=book_row_counter, column=book_column_counter, sticky="ew", padx=5, pady=5)
    book_column_counter += 1

def book_Menu_add_new_button(book):
    global book_counter
    global book_row_counter
    global book_column_counter
    book_dict[book] = {}
    if book != None:
        book_name = book
        newbtn = Button(root, fg="blue", text=book_name, height=10, width=20,
                        command=lambda: new_chapter_Menu(book_name))
        book_counter += 1
        if ((book_counter) % 5) == 0:
            book_row_counter += 1
            book_column_counter = 0

        newbtn.grid(row=book_row_counter, column=book_column_counter, sticky="ew", padx=5, pady=5)
        book_column_counter += 1
    pass

def book_name():

   string= entry.get()
   book = string
   if book in book_dict:
       small.destroy()
       same_error_Input()
   else:
       if book != None:
          small.destroy()
          book_Menu_add_new_button(book)
          new_chapter_Menu(book)
          createTable(conn, book)

def same_error_Input():
   global small
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Book Name Already Taken", font=("Courier 12 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()
   tk.Button(small, text="Okay", width=20, command=book_name).pack(pady=20)


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


def delete_chapter(book_title, chapter_title):
    book_dict[book_title][chapter_title] = ("","")
    del book_dict[book_title][chapter_title]

    new.destroy()

    openBook(book_dict[book_title],book_title)

def new_chapter_Menu(book_title):
    global chptrMenu

    try:
        store = book_dict[book_title]
    except:
        store = None

    if store == None:
        chptrMenu = Toplevel(root)
        chptrMenu.geometry("800x800")
        for i in range(4):
            chptrMenu.columnconfigure(i, weight=5, minsize=50)
            chptrMenu.rowconfigure(i, weight=5, minsize=50)
        chptrMenu.title(book_title)
        chptrbtn = Button(chptrMenu, fg="blue", text='New Chapter', height=10, width=20,
                          command=lambda: chapter_Input(book_title))

        chptrbtn.grid(row=0, column=0)
    else:
        print("new_chapter_Menu")
        openBook(store,book_title)



def chapter_Menu_add_button(book_title, chapter_title):
    global chapter_counter
    global chapter_row_counter
    global chapter_column_counter

    chapters = book_dict[book_title]
    if chapter_title != None:
        chapter_name = chapter_title
        newbtn = Button(chptrMenu, fg="blue", text=chapter_title, height=10, width=20,
                        command=lambda: openChapter(book_title, chapter_title, chapters))
        chapter_counter += 1

        if ((chapter_counter) % 5) == 0:
            chapter_row_counter += 1
            chapter_column_counter = 0

        newbtn.grid(row=chapter_row_counter, column=chapter_column_counter)
        chapter_column_counter += 1

def chapter_name(book):

   string= entry.get()
   chapter_title = string

   chapter_list = book_dict[book].keys()
   if chapter_title in chapter_list:
       small.destroy()
       same_chapter_Input_ERROR(book)
   else:
       if chapter_title != None:
          small.destroy()

          Text_Editor(book,chapter_title)

def same_chapter_Input_ERROR(book):
   global small
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Chapter Already Taken", font=("Courier 22 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()

   # Create a Button to validate Entry Widget
   tk.Button(small, text="Okay", width=20, command=lambda: chapter_name(book)).pack(pady=20)

def chapter_Input(book):
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
   tk.Button(small, text="Okay", width=20, command=lambda: chapter_name(book)).pack(pady=20)



def Text_Editor(book, chapter_title):
    # textArea: variable holding our top text editor window
    # questArea: variable holding our bottom text editor window
    # new: variable holding the frame containing our text editors
    global textArea
    global questArea
    global new
    global prmptFrame


    new = Toplevel(root)
    textFrame = Frame(new,width=300, height=400)
    questFrame = Frame(new, width=300, height=100)
    textArea = tk.Text(textFrame)
    questArea = tk.Text(questFrame)

    btnFrame = tk.Frame(new)
    prmptFrame = tk.Frame(new)

    btnSave = tk.Button(btnFrame, text = "save", command=lambda: saveFile(book, chapter_title))
    btnChptr = tk.Button(btnFrame, text = "new chapter", command=lambda: chapter_Input(book))
    btnPrompt = tk.Button(prmptFrame, text = "Toggle SQ3R", command=promptToggle)
    btnDelete = tk.Button(btnFrame, text="delete", command=lambda: delete_chapter(book, chapter_title))
    btnDelete.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    btnBlock = tk.Button(btnFrame, text="Toggle Block", command=questToggle)
    btnBlock.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    #textArea.grid(sticky= N + E + S + W)
    #questArea.grid(sticky=N + E + S + W)

    # creates scroll bar
    #ScrollBar = Scrollbar(textArea)

    new.title(book + "-" + chapter_title)

    new.protocol("WM_DELETE_WINDOW", on_closing)

    menuBar = Menu(new)
    new.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openChapter)
    fileMenu.add_command(label="Save", command=lambda:saveFile(book,chapter_title))
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

def saveFile(book,chapter_title):
    '''
    saveas = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                      defaultextension=".txt",
                                      filetypes = [("All Files", "*.*"),
                                                    ("Test Documents", "*.txt")])
    '''
    toggle = True
    if chapter_title in book_dict[book].keys():
        toggle = False
    #print(book_dict)
    #print(book_dict[book].keys())
    print("saveFile- book:", book)
    print("saveFile- chapter:", chapter_title)
    notes = textArea.get(1.0,END)
    questions = questArea.get(1.0, END)
    # This will save as {book:{chapter_title:(notes, questions)}}
    book_dict[book][chapter_title] = (notes, questions)
    #print(book_dict)

    if toggle:
        #toggle is True if chapter_title is NOT in book_dict[book]
        chapter_Menu_add_button(book, chapter_title)
        #createTable(conn, book)
    #print(book)
    addNote(conn, book, chapter_title, notes, questions)


    #print(book_dict[book_title][chapter_title][0])
    #print(book_dict[book_title][chapter_title][1])


def newFile():
    global textArea
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openBook(chapters,book):
    # creates the chapter menu and adds all the chapters it contains
    global chptrMenu
    global chapter_counter

    try:
        chptrMenu.destroy()
    except:
        pass

    chapter_dict = chapters
    book_title = book
    chptrMenu = Toplevel(root)
    chptrMenu.geometry("800x800")
    for i in range(4):
        chptrMenu.columnconfigure(i, weight=5, minsize=50)
        chptrMenu.rowconfigure(i, weight=5, minsize=50)
    chptrMenu.title(book)
    chptrbtn = Button(chptrMenu, fg="blue", text='New Chapter', height=10, width=20,
                      command=lambda: chapter_Input(book))
    chptrbtn.grid(row=0, column=0)

    # goes thru list of all chapter names in chapter_dict
    chpt_list = chapter_dict.keys()
    for item in chpt_list:

        if item != None:
            # adds button to menu for every chapter in book upon open
            chapter_name = item

            chapter_Menu_add_button(book,chapter_name)


def openChapter(book_title, chapter_name, chapters):
    global textArea

    book = book_dict[book_title]
    try:
        textArea.delete(1.0, END)
        questArea.delete(1.0, END)
    except:
        Text_Editor(book_title, chapter_name)
        pass

    notes = chapters[chapter_name][0]
    questions = chapters[chapter_name][1]
    textArea.insert("1.0", notes)
    questArea.insert("1.0", questions)

    pass

def menu_close():
    if messagebox.askokcancel("Quit", "Do you want to quit without saving?"):

        root.destroy()

# asks user if they are sure they want to quit
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit without saving?"):

        new.destroy()


# these dictionaries need to come from somewhere else (database)

book_Menu()

