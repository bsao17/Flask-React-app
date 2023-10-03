import mysql.connector
from mysql.connector import Error

AUTHLIB_INSECURE_TRANSPORT = True


class Database:
    def __init__(self, uri, database, username, password):
        self.URI = uri
        self.DATABASE = database
        self.USERNAME = username
        self.PASSWORD = password

    def query(self, query):
        with mysql.connector.connect(
                host=self.URI,
                database=self.DATABASE,
                user=self.USERNAME,
                password=self.PASSWORD,
        ) as con:
            if con.is_connected():
                print("Vous êtes connecté à la base de données !")
                cursor = con.cursor()
                cursor.execute(query)
                return cursor.fetchone()
            con.close()


acn_database = Database('localhost', 'acn_blog', 'root', 'root')

try:
    user_table = acn_database.query("SHOW TABLE STATUS FROM `acn_blog`;")
    rows = user_table
    print(rows)
except Error as e:
    print(f"Connexion impossible, {e.msg} !")
