import os

import dotenv
from flask_cors import CORS
from models import Database
from dotenv import load_dotenv

from flask import Flask, render_template
from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, IntegerField, BooleanField, RadioField, DateField, validators
from wtforms.validators import InputRequired, Length

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
CORS(app)


class Todo_Form(FlaskForm):
    user = StringField(validators=[InputRequired(), Length(min=1, max=50)])
    date = DateField('Date', format='%d-%m-%Y')
    task = TextAreaField(validators=[InputRequired(), Length(max=200)])
    closed = BooleanField('Available', default='checked')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])


@app.route("/", methods=('GET', 'POST'))
def index():
    form = RegistrationForm()
    return render_template("index.html", form=form)


@app.route('/tasks')
def tasks():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SELECT * FROM `acn_blog`.`tasks` LIMIT 1000;")
    return [data]


@app.route('/database')
def database():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SELECT * FROM `acn_blog`.`users` LIMIT 1000;")
    return [data]


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500
