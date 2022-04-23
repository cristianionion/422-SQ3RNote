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
    query = "CREATE TABLE IF NOT EXISTS "+str(book)+" (note_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(2000),chapter VARCHAR(2000), survey VARCHAR(2000), question VARCHAR(2000), readd VARCHAR(2000), revieww VARCHAR(2000), recitee VARCHAR(2000))"
    mycursor.execute(query)
    
# small test
bookinput = "book2"
db_create_table(conn, bookinput)


def db_insert_note(conn,table, title,chapter, survey, question, readd, revieww, recitee):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO "+str(table)+" (title, chapter,survey,question,readd,revieww,recitee) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = (title,chapter, survey, question, readd, revieww, recitee)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

#small test
db_insert_note(conn, bookinput,"t","c","s","q","r","r","r")
    

# FUNCTION FOR UPDATING SQ3R in db
def db_update_all(conn,table, title,chapter,survey,question,read ,review,recite, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE "+str(table)+" SET title = %s,chapter = %s, survey = %s,question = %s,readd = %s, revieww = %s, recitee = %s WHERE note_id = %s"
    val = (title,chapter,survey,question,read, review,recite, note_id)
    mycursor.execute(query, val)
    conn.commit()

#small test
db_update_all(conn,bookinput, "fake title","fake chapter","fake survey" ,"fake question","fake read","fake review","fake recite", "1")



def db_select_all_notes(conn,table):
    conn.database = "db_notes"
    query = "SELECT * from "+ str(table)
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def db_select_specific_note(conn,table, note_id):
    print(note_id, "THIS IS THE NOTE ID")
    print("AHAHAHAHA", "nodeID"+str(note_id))
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title,chapter, survey,question, readd, revieww, recitee FROM "+str(table)+" WHERE note_id = " + str(note_id))
    return mycursor.fetchone()

#small tests
print(db_select_all_notes(conn,bookinput))
print(db_select_specific_note(conn,bookinput,2))


def db_delete_note(conn,table, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM "+str(table)+" WHERE note_id = %s"
    adr = (note_id,)
    mycursor.execute(query, adr)
    conn.commit()

#db_delete_note(conn,bookinput,"3")
