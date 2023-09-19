import time

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='to-do/build', static_folder='static')


@app.route('/')
def home():
    return render_template("index.html")