"""
ARA.py
Group 4: Tiana Cook, Jake Follett, Cristian Ion, Wanrong Qi, Jack White.
Created on: 4/10/2022
Last modified on: 4/25/2022
Description: This is the code for student to run the program and start note-taking.
References: https://levelup.gitconnected.com/build-a-note-taking-app-with-mysql-backend-in-python-927b4c5fad91
https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets
https://stackoverflow.com/questions/4236182/generate-tkinter-buttons-dynamically
https://www.studytonight.com/tkinter/text-editor-application-using-tkinter

"""

"""
All the modules that we need to import
"""
from tkinter import * # used for GUI
import tkinter as tk
from tkinter import messagebox
import os
from main import * # connect with the database


def book_Menu():
    '''This method creates the menu of all the book titles,
    along with the button to create new books'''

    # root: the root of our tkinter windows
    global root
    # create a book_dict where all the book information will be stored
    global book_dict


    # book_counter: keeps track of how many books exist
    # chapter_counter: keeps track of how many chapters are in a book upon its selection
    global book_counter
    global chapter_counter

    # book_row_counter: keeps track of how many rows of buttons are in the book menu
    # book_column_counter: keeps track of how many columns of buttons are in the book menu
    global book_row_counter
    global book_column_counter

    # chapter_row_counter: keeps track of how many rows of buttons are in a book's chapter menu
    # chapter_column_counter: keeps track of how many columns of buttons are in a book's chapter menu
    global chapter_row_counter
    global chapter_column_counter

    # prompt_list: a list holding the text of the SQ3R prompts
    global prompt_list

    # prmptBool: keeps track of whether SQ3R prompts are enabled in a chapter
    # blockBool: keeps track of whether the quiz mode is enabled in a chapter
    global prmptBool
    global blockBool
    blockBool = False
    prmptBool = True

    # This will prompt when the user clicks the Toggle SQ3R
    prompt_list = [
        "Survey: Scan the text and pay attention to headings, section titles, pictures and graphs to get the big idea.\n",
        "Question: Ask yourself some questions that you’d like to know the answer to after reading the text.\n",
        "Read: Read the text and take note of your readings. Try to find answers to your questions.\n",
        "Recite: Repeat important parts or a summary of what you have read.\n",
        "Review: Look back on your notes and try to review the idea of the text you’ve read.\n"]

    # book_column_counter set at 1 because the 'New Book' button takes up the first column
    # book_row_counter set at 0 because all book buttons start on row 0
    book_column_counter = 1
    book_row_counter = 0

    # chapter_column_counter set at 1 because the 'New Chapter' button takes up the first column
    # chapter_row_counter set at 0 because all chapter buttons start on row 0
    chapter_column_counter = 1
    chapter_row_counter = 0

    # stores our database of book notes in a dictionary
    book_dict = db_convert_to_dictionary()

    # chapter_counter set at 0 because no book has been selected
    chapter_counter = 0

    # creates our root tkinter window
    root = tk.Tk()

    # sets the header of the book menu window
    root.title("Book Menu")

    # protocol if the root window is exited out of
    root.protocol("WM_DELETE_WINDOW", menu_close)

    # book_counter starts at 0 and is increased as book titles are added to the menu
    book_counter = 0

    # Initialize tkinter window with dimensions 800 x 800
    root.geometry('800x800')

    # this enables the book menu buttons to reformat in response to window resizing
    for i in range(4):
        root.columnconfigure(i, weight=5, minsize=50)
        root.rowconfigure(i, weight=5, minsize=50)

    # creates a 'New Book' Button
    btn1 = Button(root, fg="blue", text='New Book', height=10, width=20,
                  command=book_Input)

    # places the 'New Book' Button
    btn1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    # book_list: list of all book keys (titles)
    book_list = book_dict.keys()


    # goes thru book_list, creating a button for every book title
    for item in book_list:

        if item != None:
            book_Menu_add_button(item)

    # keeps window(s)up
    root.mainloop()

def promptToggle():
    '''This toggles the SQ3R prompt on and off'''
    global prmptFrame
    global prmptBool
    global labelPrompt
    # if prmptBool is True it means the SQ3R prompt is turned off
    if prmptBool:
        # prompt holds the string of our SQ3R prompts
        prompt = prompt_list[0] + prompt_list[1] + prompt_list[2] + prompt_list[3] + prompt_list[4]
        # creates the label to hold the prompts
        labelPrompt = tk.Label(prmptFrame, text=prompt)
        # places the label in the window
        labelPrompt.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        # prmptBool is set to False because the prompt is on
        prmptBool = False
    else:
        # if the SQ3R prompt is on it turns off prompt mode by destroying the label containing the prompts
        labelPrompt.destroy()
        # prmptBool is set to True because the prompt is off
        prmptBool = True


def questToggle():
    '''This toggles the quiz mode on and off'''
    global new
    global blockFrame
    global blockBool
    # if blockBool is True it means the quiz mode is on
    if blockBool:
        # if quiz mode is on it turns off quiz mode by destroying the label blocking the notes
        blockFrame.destroy()
        # blockBool is set to False because it is now off
        blockBool=False
    else:
        # if quiz mode is off it turns on quiz mode by creating a label blocking the notes
        blockFrame = Frame(new, width=300, height=400, bg="white")
        # places the label over the textArea
        blockFrame.grid(row=0, column=1, sticky="nsew")
        # blockBool is set to True because it is now on
        blockBool=True


def book_Menu_add_button(book_title):
    '''This method creates the buttons for books already existing in the database upon startup'''
    global book_counter
    global book_row_counter
    global book_column_counter

    # chapters contains dictionary of book_title's chapters
    chapters = book_dict[book_title]

    # creates a button for the pre-existing book title
    newbtn = Button(root, fg="blue", text=book_title, height=10, width=20,
                    command=lambda: openBook(chapters, book_title))


    # calculates the necessary placement of the book button:
    # the menu is set up to have a maximum of 5 columns of buttons
    # every time the book_counter is divisible by 0 book_row_counter is increased by 1
    # this places the book buttons on the row below the previously placed buttons
    book_counter += 1
    if (book_counter % 5) == 0:
        book_row_counter += 1
        book_column_counter = 0

    # places the button
    newbtn.grid(row=book_row_counter, column=book_column_counter, sticky="ew", padx=5, pady=5)
    book_column_counter += 1


def book_name():
   '''retrieves the user input for a new book title and calls the necessary functions to create it'''
   # stores the user input in string
   string = entry.get()
   book = string
   if book != None:
       # replaces spaces in the book title with a special character that can be stored in our database
       book_with_space = book.replace(" ", "あ")

   # checks if the book title already exists in our book dictionary
   if book in book_dict:
       # destroys the text input window if the titled entered is not a new book
       small.destroy()
       # creates a new text input window telling the user to input a new title
       same_error_Input()
   else:
       if book != None:
          # destroys the text input window if the titled entered is a new book
          small.destroy()
          # adds a button to the book menu
          new_book_Menu_add_button(book)
          # creates the chapter menu of the new book
          new_chapter_Menu(book)
          # creates a table for our book to be stored in the database
          createTable(conn, book_with_space)

def same_error_Input():
   '''This method creates a new user input window if the book title they entered is already taken'''
   global small
   # creates a window for text entry if the entered book name is already taken
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Book Name Already Taken", font=("Courier 12 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()
   # creates a button for the user to click upon entering the title
   tk.Button(small, text="Okay", width=20, command=book_name).pack(pady=20)


def book_Input():
   '''This method creates a user input window for the book title'''
   global small
   # creates a window for text entry when the 'New Book' button is selected
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Book Name", font=("Courier 22 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()
   # creates a button for the user to click upon entering the title
   tk.Button(small, text="Okay", width=20, command=book_name).pack(pady=20)


def delete_chapter(book_title, chapter_title):
    '''Deletes all the contents of a chapter, the button in the chapter menu,
    and the chapter in the database'''
    global chapter_counter
    global chapter_row_counter
    global chapter_column_counter
    # removes all text from the chapter
    book_dict[book_title][chapter_title] = ("","")
    # deletes the chapter entry in its book's dictionary
    del book_dict[book_title][chapter_title]


    chapter_counter = 0
    chapter_row_counter = 0
    chapter_column_counter = 1

    # closes the chapter menu window so ti can be updated
    new.destroy()

    # deletes chapter notes from the database
    deleteNote(conn, book_title, chapter_title)

    # reopens the updated chapter menu
    openBook(book_dict[book_title],book_title)

def new_chapter_Menu(book_title):
    '''Creates the chapter menu for a book that is selected or created'''
    global chptrMenu

    # tries to retrieve the book_title's chapter dictionary from the book dictionary
    try:
        store = book_dict[book_title]
    except:
        # assigns store to None if the entry in the book dictionary doesn't exist
        store = None

    # if store==None then the book is a new title
    if store == None:
        # creates the chapter menu
        chptrMenu = Toplevel(root)
        chptrMenu.geometry("800x800")
        # this enables the book menu buttons to reformat in response to window resizing
        for i in range(4):
            chptrMenu.columnconfigure(i, weight=5, minsize=50)
            chptrMenu.rowconfigure(i, weight=5, minsize=50)

        # assigns the chapter menu header to the book title
        chptrMenu.title(book_title)
        # creates 'New Chapter' button in the chapter menu
        chptrbtn = Button(chptrMenu, fg="blue", text='New Chapter', height=10, width=20,
                          command=lambda: chapter_Input(book_title))
        # places chapter button
        chptrbtn.grid(row=0, column=0)
    else:

        # if the book_title already exists in our dictionary it calls our openBook() function
        openBook(store,book_title)


def new_book_Menu_add_button(book):
    '''Creates the button for a newly added book title in the book menu'''
    global book_counter
    global book_row_counter
    global book_column_counter

    # adds the new book title to the book dictionary, giving it the value of an empty dictionary
    book_dict[book] = {}

    # checks if book holds a title
    if book != None:
        # creates a button on the book menu which creates the chapter menu upon selection
        book_name = book
        newbtn = Button(root, fg="blue", text=book_name, height=10, width=20,
                        command=lambda: new_chapter_Menu(book_name))

        # calculates placement of added button:
        # the menu is set up to have a maximum of 5 columns of buttons
        # every time the chapter_counter is divisible by 0 chapter_row_counter is increased by 1
        # this places the chapter buttons on the row below the previously placed buttons
        book_counter += 1
        if ((book_counter) % 5) == 0:
            book_row_counter += 1
            book_column_counter = 0

        # places button
        newbtn.grid(row=book_row_counter, column=book_column_counter, sticky="ew", padx=5, pady=5)
        book_column_counter += 1


def chapter_Menu_add_button(book_title, chapter_title):
    '''Creates the button for a book title already existing in the database'''
    global chapter_counter
    global chapter_row_counter
    global chapter_column_counter

    chapters = book_dict[book_title]
    if chapter_title != None:
        # adds button to the chapter menu for chapters already in the database
        newbtn = Button(chptrMenu, fg="blue", text=chapter_title, height=10, width=20,
                        command=lambda: openChapter(book_title, chapter_title, chapters))

        # calculates placement of added button:
        # the menu is set up to have a maximum of 5 columns of buttons
        # every time the chapter_counter is divisible by 0 chapter_row_counter is increased by 1
        # this places the chapter buttons on the row below the previously placed buttons
        chapter_counter += 1
        if ((chapter_counter) % 5) == 0:
            chapter_row_counter += 1
            chapter_column_counter = 0

        # places button
        newbtn.grid(row=chapter_row_counter, column=chapter_column_counter)
        chapter_column_counter += 1

def chapter_name(book):
   '''retrieves the user input for a new chapter name'''
   # stores the user input in string
   string= entry.get()
   chapter_title = string
   # creates list of all the chapters in the selceted book's dictionary
   chapter_list = book_dict[book].keys()
   # checks if the chapter_title is in the chapter_list
   if chapter_title in chapter_list:
       # destroys the text input window if the titled entered is not a new chapter
       small.destroy()
       # creates a new text input window telling the user to input a new chapter title
       same_chapter_Input_ERROR(book)
   else:
       if chapter_title != None:
           # destroys the text input window if the titled entered is a new chapter
          small.destroy()

          # creates the new chapter window
          Text_Editor(book,chapter_title)

def same_chapter_Input_ERROR(book):
   '''This method creates a new user input window if the chapter title they entered is already taken'''
   global small
   # creates a window for text entry if the entered chapter name is already taken
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Chapter Already Taken", font=("Courier 12 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()

   # Create a Button to validate Entry Widget
   tk.Button(small, text="Okay", width=20, command=lambda: chapter_name(book)).pack(pady=20)

def chapter_Input(book):
   '''This method creates a user input window for the chapter title'''
   global small
   # creates a window for text entry when the 'New Chapter' button is selected
   small = Toplevel(root)
   small.geometry("300x300")
   label = Label(small, text="Chapter Name", font=("Courier 22 bold"))
   label.pack()

   # Create an Entry widget to accept User Input
   global entry
   entry = Entry(small, width=40)

   entry.focus_set()
   entry.pack()

   # Create a Button to validate Entry Widget
   tk.Button(small, text="Okay", width=20, command=lambda: chapter_name(book)).pack(pady=20)



def Text_Editor(book, chapter_title):
    '''Creates the window containing the note and question text editors along with their buttons'''
    # textArea: variable holding the top text editor window
    # questArea: variable holding the bottom text editor window
    # new: variable holding the frame containing the text editors
    # prmptFrame: variable holding the frame of the SQ3R prompt text
    global textArea
    global questArea
    global new
    global prmptFrame

    # creates the a new window and assigns it to new
    new = Toplevel(root)
    # the frame where our notes text editor will be stored
    textFrame = Frame(new,width=300, height=400)
    # the frame where our questions text editor will be stored
    questFrame = Frame(new, width=300, height=100)

    # creates the text editor in the textFrame
    textArea = tk.Text(textFrame)
    # creates the text editor in the questFrame
    questArea = tk.Text(questFrame)

    # creates the frame to hold the buttons
    btnFrame = tk.Frame(new)
    # creates the frame to hold the SQ3R prompts
    prmptFrame = tk.Frame(new)

    # creates the save button which calls saveFile()
    btnSave = tk.Button(btnFrame, text = "save", command=lambda: saveFile(book, chapter_title))
    # creates the new chapter button which calls chapter_Input()
    btnChptr = tk.Button(btnFrame, text = "new chapter", command=lambda: chapter_Input(book))
    # creates the "Toggle SQ3R" button which calls promptToggle()
    btnPrompt = tk.Button(prmptFrame, text = "Toggle SQ3R", command=promptToggle)
    # creates the "delete" button which calls delete_chapter()
    btnDelete = tk.Button(btnFrame, text="delete", command=lambda: delete_chapter(book, chapter_title))
    # creates the "Toggle Quiz" button which calls questToggle()
    btnBlock = tk.Button(btnFrame, text="Toggle Quiz", command=questToggle)

    #textArea.grid(sticky= N + E + S + W)
    #questArea.grid(sticky=N + E + S + W)

    # creates scroll bar
    #ScrollBar = Scrollbar(textArea)

    # creates the header for the chapter window
    new.title(book + "-" + chapter_title)

    # creates the protocol for if the chapter window is closed
    new.protocol("WM_DELETE_WINDOW", on_closing)



    # makes text box horizontally resizable (do we want this?)
    #root.grid_rowconfigure(0, weight=1)
    new.grid_columnconfigure(0, weight=1)

    # places button on grid:
    #   "ew" : forces buttons to expand horizontally
    #   padx/pady : horizontal/vertical padding given to button

    # places the buttons in btnFrame
    btnSave.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btnChptr.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    btnDelete.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    btnBlock.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    # places the textArea (notes text editor) in the window
    textArea.grid(row=0, column=1, sticky="nsew")
    # places the questArea (questions text editor) in the window
    questArea.grid(row=1, column=1, sticky="nsew")
    # places the btnPrompt in prmptFrame
    btnPrompt.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


    # creates grid, with distinct columns for button frames and text editor frames
    # btnFrame, textFrame, and prmptFrame are placed on the same row but different columns
    btnFrame.grid(row=0, column=0, sticky="ns")
    prmptFrame.grid(row=0, column=2, sticky="ns")
    textFrame.grid(row=0, column=1, sticky="nsew")

    # questFrame is placed in the same column and a row below textFrame
    questFrame.grid(row=1, column=1)



    # implements scroll bar
    #ScrollBar.pack(side=RIGHT, fill=Y)
    #ScrollBar.config(command=textArea.yview)
    #textArea.config(yscrollcommand=ScrollBar.set)

def saveFile(book,chapter_title):
    '''this saves the contents of a chapter to the database'''
    toggle = True
    if chapter_title in book_dict[book].keys():
        toggle = False


    notes = textArea.get(1.0,END)
    questions = questArea.get(1.0, END)
    # This will save as {book:{chapter_title:(notes, questions)}}
    book_dict[book][chapter_title] = (notes, questions)


    if toggle:
        #toggle is True if chapter_title is NOT in book_dict[book]
        chapter_Menu_add_button(book, chapter_title)
        #createTable(conn, book)

    # This will add all the book information to the database by
    # calling the addNote function on the main file
    addNote(conn, book, chapter_title, notes, questions)




def openBook(chapters,book):
    '''This function creates a chapter menu containing the contents of the selected book'''
    # creates the chapter menu and adds all the chapters it contains
    global chptrMenu
    global chapter_counter

    global chapter_row_counter
    global chapter_column_counter

    # resets chapter_counter, chapter_row_counter, and chapter_column_counter
    # because a new chapter Menu is being created
    chapter_counter = 0
    chapter_row_counter = 0
    chapter_column_counter = 1

    # destroys chptrMenu if the window is open
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
    '''this creates the window for an pre-existing chapter selected by the user in the chapter menu'''
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
    '''protocol called if the book menu window is closed:
    notifies the user this will close all windows'''
    if messagebox.askokcancel("Quit", "Do you want to quit? This will close all windows."):

        root.destroy()

# asks user if they are sure they want to quit
def on_closing():
    '''protocol called if the chapter text editor window is closed:
    asks if the user wants to quit without saving'''
    if messagebox.askokcancel("Quit", "Do you want to quit without saving?"):

        new.destroy()



book_Menu()



