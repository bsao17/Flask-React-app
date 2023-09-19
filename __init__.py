import sys
import mysql.connector
from mysql.connector import Error

print(f"Connexion à la base de donnée !")


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='acn_blog',

        )
        print('Connection à la base de donnée, réussie !')
    except Error as e:
        print(f"Connexion impossible, {e.msg} empêche la connection à la base de donnée {db['db_name']}")

    return connection
