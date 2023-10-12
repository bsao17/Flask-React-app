from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, BooleanField, DateField, validators, PasswordField
from wtforms.validators import InputRequired, Length


class Todo_Form(Form):
    user = StringField(validators=[InputRequired(), Length(min=1, max=50)])
    date = DateField('Date', format='%d-%m-%Y')
    task = TextAreaField(validators=[InputRequired(), Length(max=200)])
    closed = BooleanField('Available', default='checked')


class Login_form(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.Length(min=4),
        validators.equal_to('confirm', message="Passwords must match")
    ])
    confirm = PasswordField('Repeat Password')


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.Length(min=4),
        validators.equal_to('confirm', message="Passwords must match")
    ])
    confirm = PasswordField('Repeat Password')