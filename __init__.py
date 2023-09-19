import sys
import mysql.connector
from mysql.connector import Error

print(f"Connexion à la base de donnée {sys.argv[1]} !")


def create_connection(*args):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=args[1],
            user=args[2],
            pwd=args[3]
        )
        print('Connection à la base de donnée, réussie !')
    except Error as e:
        print(f"L'erreur {e.msg} empêche la connection à la base de donnée {host_name}")

    return connection


if __name__ == '__main__':
    create_connection(sys.argv[1], sys.argv[2], sys.argv[3])
