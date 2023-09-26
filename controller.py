from flask_cors import CORS
from models import Database

from flask import Flask, render_template

app = Flask(__name__)
CORS(app)


@app.route('/users')
def users():
    return render_template('index.html')


@app.route('/database')
def database():
    data = Database().query("SELECT * FROM `acn_blog`.`users` LIMIT 1000;")
    return [data]


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500
