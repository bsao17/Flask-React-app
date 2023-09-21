from flask_cors import CORS
from models import Database
import time

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
CORS(app)


@app.route('/users')
def users():
    return render_template('index.html')


@app.route('/database')
def data():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SELECT * FROM `acn_blog`.`users` LIMIT 1000;")
    return [data]


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500
