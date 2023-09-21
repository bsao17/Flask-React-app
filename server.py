from flask_cors import CORS
from models import Database

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/users')
def users():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SHOW CREATE TABLE `acn_blog`.`users`")
    return data[0]

@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500
