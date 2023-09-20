import time
from models import Database

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/users')
def users():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SHOW CREATE TABLE `acn_blog`.`users`;")
    return render_template('tables.html', data=data)
