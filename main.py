
# import the sql driver
import mysql.connector

#conn connects to the mysql server
conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

# create the database if it does not exist
def createDatabase(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")


createDatabase(conn)


# create the database tables for each book
# which will include, book title, chapter title, notes, and questions
# table name must be 64 characters long or shorter, and cannot have spaces in the name
def createTable(conn, book):
    createDatabase(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS "+str(book)+" (chapter VARCHAR(2000), notes VARCHAR(2000), question VARCHAR(2000))"
    mycursor.execute(query)
    
# small test
#bookinput = "a234567890123456789012345678901234567890123456789012345678901234"
#createTable(conn, bookinput)


# add note function so that we can insert data into the database

def addNote(conn,table,chapter,notes, question):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO "+str(table)+" (chapter,notes,question) VALUES (%s,%s,%s)"
    val = (chapter,notes, question)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

#small test
#addNote(conn, bookinput,"chap212","n","q")
#addNote(conn,bookinput, "chapter 3", "notess","qqqqqqqqqs")
#addNote(conn,bookinput,"c11", "so many written notes", "no questions")
#addNote(conn,bookinput,"section5", "write right rite","queue quest")
    

# FUNCTION FOR UPDATING WHOLE CHAPTER NOTES in db
def updateNote(conn,table, notes, question, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE "+str(table)+" SET notes = %s,question = %s WHERE chapter = %s"
    val = (notes,question,chapter)
    mycursor.execute(query, val)
    conn.commit()

#small test
#updateNote(conn,bookinput, "fake notes" ,"fake question","c11")


# function to retrieve all data from the database
def selectAll(conn,table):
    conn.database = "db_notes"
    query = "SELECT * from "+ str(table)
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

# function to retrieve specific data from the database
# can be used to check if a chapter already has notes or not
def selectOne(conn,table, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    #print("THIS IS WHAT IT THINKS chapter is: ", str(chapter))
    #print("THIS IS WHAT IT THINKS TABLE is: ", table)
    query = "SELECT * FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    #print("CHAP TYPE: ", type(chapter), "QUERY TYPE: ", type(query))
    #print("THIS IS WHAT QUERY IS: ","SELECT * FROM "+str(table)+" WHERE chapter = chap")
    mycursor.execute(query,adr)
    return mycursor.fetchone()

#small tests
#print(selectAll(conn,bookinput))
#chap = 'chap21'
#print("THIS SHOULD WORK: ",selectOne(conn,bookinput,chap),type(selectOne(conn,bookinput,chap)))
#print("THIS should NOT WORK: ",selectOne(conn,bookinput,"chapternotreal"),type(selectOne(conn,bookinput,"chapternotreal")))

# function to delete notes in database
def deleteNote(conn,table, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    mycursor.execute(query, adr)
    conn.commit()

#deleteNote(conn,bookinput,"3")

# function to display all tables (book titles) that are saved in the database
def getTables(conn):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SHOW TABLES FROM db_notes")
    return mycursor.fetchall()

#print(getTables(conn))

def db_convert_to_dictionary():
    book = getTables(conn)
    #print(book)
    #print(len(book))
    print(len(book))
    book_dict = {}
    if book == None:
        return book_dict
    for index in range(len(book)):
        chapter_dict = {}
        book_name = book[index][0]
        #print(book_name)
        chapter_information = selectAll(conn, book_name)[0]
        #print(chapter_information)
        chapter_key = chapter_information[1]
        #print(book_name)
        chapter_notes_questions = (chapter_information[2], chapter_information[3])
        #print(chapter_notes_questions)
        #print(chapter_dict)
        chapter_dict[chapter_key] = chapter_notes_questions
        #print(chapter_dict)
        book_dict[book_name] = chapter_dict
    return book_dict

#print(db_convert_to_dictionary())


