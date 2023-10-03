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
from sqlalchemy.orm import DeclarativeBase

AUTHLIB_INSECURE_TRANSPORT = True

print("Application lancée")