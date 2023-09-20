import sys
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, uri, database, username, password):
        self.URI = uri
        self.DATABASE = database
        self.USERNAME = username
        self.PASSWORD = password

    def query(self, query):
        rows = None
        with mysql.connector.connect(
                host=self.URI,
                database=self.DATABASE,
                user=self.USERNAME,
                password=self.PASSWORD,
        ) as con:
            if con.is_connected():
                print("connexion réussie !")
                cursor = con.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    return row
        return rows


acn_database = Database('localhost', 'acn_blog', 'root', 'root')

try:
    user_table = acn_database.query("SHOW TABLE STATUS FROM `acn_blog`;")
    print(user_table)
except Error as e:
    print(f"Connexion impossible, {e.msg} !")
