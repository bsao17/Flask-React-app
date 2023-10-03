from flask import request, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

from controllers.controller import app

login_manager = LoginManager()
login_manager.init_app(app=app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.route('/login')
def Login():
    if request.method == "POST":
        user = User(request.form['email'])
        password = request.form['password']
        login_user(user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
