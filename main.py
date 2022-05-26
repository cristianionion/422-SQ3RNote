"""

main.py
Group 4: Tiana Cook, Jake Follett, Cristian Ion, Wanrong Qi, Jack White.
Created on: 4/10/2022
Last modified on: 4/25/2022
Description: This is the code for admins to access the database
References: https://levelup.gitconnected.com/build-a-note-taking-app-with-mysql-backend-in-python-927b4c5fad91

"""

# import the sql driver
import mysql.connector

#conn connects to the mysql server
conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="passpass")

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
    book = book.replace(" ","あ")
    query = "CREATE TABLE IF NOT EXISTS "+str(book)+" (title VARCHAR(2000), chapter VARCHAR(2000), notes VARCHAR(2000), question VARCHAR(2000))"
    mycursor.execute(query)



# add note function so that we can insert data into the database
def addNote(conn,table,chapter,notes, question):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    table = table.replace(" ","あ")
    query = "INSERT INTO "+str(table)+" (title,chapter,notes,question) VALUES (%s,%s,%s,%s)"
    val = (table,chapter,notes, question)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

 

# FUNCTION FOR UPDATING WHOLE CHAPTER NOTES in db
def updateNote(conn,table, notes, question, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE "+str(table)+" SET notes = %s,question = %s WHERE chapter = %s"
    val = (notes,question,chapter)
    mycursor.execute(query, val)
    conn.commit()


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

    query = "SELECT * FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    
    mycursor.execute(query,adr)
    return mycursor.fetchone()


# function to delete notes in database
def deleteNote(conn,table, chapter):
    table = table.replace(" ","あ")
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    mycursor.execute(query, adr)
    conn.commit()

def deleteBook(conn,table):
    table = table.replace(" ","あ")
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DROP TABLE IF EXISTS "+str(table)
    mycursor.execute(query)
    conn.commit()



# function to display all tables (book titles) that are saved in the database
def getTables(conn):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SHOW TABLES FROM db_notes")
    return mycursor.fetchall()





def db_convert_to_dictionary():
    book = getTables(conn)
    book_dict = {}
    if book == None:
        return book_dict
    for index in range(len(book)):
        chapter_dict = {}
        book_name = book[index][0]
        all_the_chapters = selectAll(conn, book_name)
        for chapters in all_the_chapters:
            chapter_key = chapters[1]
            chapter_notes_questions = (chapters[2], chapters[3])
            chapter_dict[chapter_key] = chapter_notes_questions
        book_name = book_name.replace("あ", " ")
        book_dict[book_name] = chapter_dict
    return book_dict

print(db_convert_to_dictionary())


