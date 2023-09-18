from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='build', static_folder='static')


@app.route("/")
def Index():
    return render_template("index.html")
