import mysql.connector
from mysql.connector import Error
import os
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, BooleanField, DateField, validators, PasswordField
from wtforms.validators import InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase
from colorama import Fore, Back, Style, init

init()
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + Back.BLUE + "To-Do application started" + Style.RESET_ALL)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
