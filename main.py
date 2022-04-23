
# import the sql driver
import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

# create the database if it does not exist
def createDatabase(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")


createDatabase(conn)


# create the database tables
# which will include, book title, chapter title, notes, and questions

def createTable(conn, book):
    createDatabase(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS "+str(book)+" (chapter VARCHAR(2000), notes VARCHAR(2000), question VARCHAR(2000))"
    mycursor.execute(query)
    
# small test
bookinput = "book20"
createTable(conn, bookinput)


# insert note function so that we can insert data into the database


def addNote(conn,table,chapter,notes, question):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO "+str(table)+" (chapter,notes,question) VALUES (%s,%s,%s)"
    val = (chapter,notes, question)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

#small test
addNote(conn, bookinput,"chap212","n","q")
    

# FUNCTION FOR UPDATING SQ3R in db
def updateNote(conn,table, notes, question, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE "+str(table)+" SET notes = %s,question = %s WHERE chapter = %s"
    val = (notes,question,chapter)
    mycursor.execute(query, val)
    conn.commit()

#small test
updateNote(conn,bookinput, "fake notes" ,"fake question","chap21")


# function to retrieve all data from the database
def selectAll(conn,table):
    conn.database = "db_notes"
    query = "SELECT * from "+ str(table)
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

# function to retrieve specific data from the database
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
print(selectAll(conn,bookinput))
chap = 'chap21'
print("THIS SHOULD WORK: ",selectOne(conn,bookinput,chap))

# function to delete notes in database
def deleteNote(conn,table, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    mycursor.execute(query, adr)
    conn.commit()

#deleteNote(conn,bookinput,"3")

def getTables(conn):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SHOW TABLES FROM db_notes")
    return mycursor.fetchall()

print(getTables(conn))