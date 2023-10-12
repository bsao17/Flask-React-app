import os
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from colorama import Fore, Back, Style, init

init()
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + Back.BLUE + "To-Do application started" + Style.RESET_ALL)


class Base(DeclarativeBase):
    pass


load_dotenv(dotenv_path=".flaskenv")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app=app)

CORS(app)
