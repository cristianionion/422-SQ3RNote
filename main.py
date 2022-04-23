import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def db_create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")

db_create_db(conn)


#
def db_create_table(conn, book):
    db_create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS "+str(book)+" (title VARCHAR(2000),chapter VARCHAR(2000), notes VARCHAR(2000), question VARCHAR(2000))"
    mycursor.execute(query)
    
# small test
bookinput = "book20"
db_create_table(conn, bookinput)


def db_insert_note(conn,table, title,chapter,notes, question):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO "+str(table)+" (title, chapter,notes,question) VALUES (%s,%s,%s,%s)"
    val = (title,chapter,notes, question)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

#small test
db_insert_note(conn, bookinput,"t","c3","n","q")
    

# FUNCTION FOR UPDATING SQ3R in db
def db_update_all(conn,table, notes, question, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE "+str(table)+" SET notes = %s,question = %s WHERE chapter = %s"
    val = (notes,question,chapter)
    mycursor.execute(query, val)
    conn.commit()

#small test
db_update_all(conn,bookinput, "fake notes" ,"fake question","c")



def db_select_all_notes(conn,table):
    conn.database = "db_notes"
    query = "SELECT * from "+ str(table)
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def db_select_specific_note(conn,table, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title,chapter, notes,question FROM "+str(table)+" WHERE chapter = " + str(chapter))
    return mycursor.fetchone()

#small tests
print(db_select_all_notes(conn,bookinput))
print(db_select_specific_note(conn,bookinput,2))


def db_delete_note(conn,table, chapter):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM "+str(table)+" WHERE chapter = %s"
    adr = (chapter,)
    mycursor.execute(query, adr)
    conn.commit()

#db_delete_note(conn,bookinput,"3")
