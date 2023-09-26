import mysql.connector
from mysql.connector import Error
import sqlite3
import os


class Database:
    database_file = 'myDatabase.db'
    conn = sqlite3

    def __init__(self):
        if os.path.isfile(self.database_file):
            self.conn.connect(self.database_file)
        else:
            self.conn.connect(self.database_file)

    def query(self, query):
        cursor = sqlite3.Cursor(sqlite3.Connection(self.database_file))
        result = cursor.execute(query)
        print(result.fetchall())
        print(f"connexion à {self.conn} !")
        return result.fetchone()    

acn_database = Database()

try:
    user_table = acn_database.query("SELECT COUNT(*) FROM 'users';")
    rows = user_table
    print(rows)
except Error as e:
    print(f"Connexion impossible, {e.msg} !")
