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