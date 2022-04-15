import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")


def db_create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db")

#invoke the function


db_create_db(conn)