import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def db_create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")

db_create_db(conn)


def db_create_table(conn):
    db_create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS FINAL_new_tb (note_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(2000),chapter VARCHAR(2000), survey VARCHAR(2000), question VARCHAR(2000), readd VARCHAR(2000), revieww VARCHAR(2000), recitee VARCHAR(2000))"
    mycursor.execute(query)
    
# invoking the function
db_create_table(conn)


def db_insert_note(conn, title,chapter, survey, question, readd, revieww, recitee):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO FINAL_new_tb (title, chapter,survey,question,readd,revieww,recitee) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = (title,chapter, survey, question, readd, revieww, recitee)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid


records = [
        ('My first title', 'Chapter1', 'survey1', 'question1', 'readd1', 'revieww1', 'recitee1'),
        ('My 2nd title', 'Chapter2', 'survey2', 'question2', 'readd2', 'revieww2', 'recitee2'),
        ('My 3rd title', 'Chapter3', 'survey3', 'question3', 'readd3', 'revieww3', 'recitee3'),
    ]

for v in records:
    db_insert_note(conn, v[0], v[1],v[2],v[3],v[4],v[5],v[6]) # invoke function



def db_select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from FINAL_new_tb"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def db_select_specific_note(conn, note_id):
    print(note_id, "THIS IS THE NOTE ID")
    print("AHAHAHAHA", "nodeID"+str(note_id))
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title,chapter, survey,question, readd, revieww, recitee FROM FINAL_new_tb WHERE note_id = " + str(note_id))
    return mycursor.fetchone()

# invoking the functions
print("=====Selecting all records =====")
data = db_select_all_notes(conn)  # select all notes
for d in data:
    print(d)
    
print("=====Selecting record where note_id is 2=====")
print(db_select_specific_note(conn, 2))
a = db_select_specific_note(conn, 2)
print(a)



### this can be applied to all aspects of notes, not just survey, functionally works
def db_update_survey(conn, title, survey, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE FINAL_new_tb SET title = %s, survey = %s WHERE note_id = %s"
    val = (title, survey, note_id)
    mycursor.execute(query, val)
    conn.commit()

def db_update_review(conn, title, review, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE FINAL_new_tb SET title = %s, revieww = %s WHERE note_id = %s"
    val = (title, review, note_id)
    mycursor.execute(query, val)
    conn.commit()

def db_update_review(conn, title, review, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE FINAL_new_tb SET title = %s, revieww = %s WHERE note_id = %s"
    val = (title, review, note_id)
    mycursor.execute(query, val)
    conn.commit()


# FUNCTION FOR UPDATING SQ3R in db
def db_update_all(conn, title,chapter,survey,question,read ,review,recite, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE FINAL_new_tb SET title = %s,chapter = %s, survey = %s,question = %s,readd = %s, revieww = %s, recitee = %s WHERE note_id = %s"
    val = (title,chapter,survey,question,read, review,recite, note_id)
    mycursor.execute(query, val)
    conn.commit()

db_update_all(conn, "fake title","fake chapter","fake survey" ,"fake question","fake read","fake review","fake recite", "1")

# invoking the function
#db_update_survey(conn, "Title1 - updated", "Survey1 - updated", "1")

rand_review = "attempt 2"
#db_update_review(conn, "Title2 - updated", rand_review, "2")

def db_delete_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM FINAL_new_tb WHERE note_id = %s"
    adr = (note_id,)
    mycursor.execute(query, adr)
    conn.commit()

# invoking the function 
# delete works, its commented out to not always delete 
#db_delete_note(conn, "2") 


#ALL above functions work as wanted

