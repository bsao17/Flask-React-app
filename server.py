import time
import models

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/users')
def users():
    data = models.query_db('SHOW TABLES FROM \'acn_blog\'')
    return render_template('tables.html', **data)


