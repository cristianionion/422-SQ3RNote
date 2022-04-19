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