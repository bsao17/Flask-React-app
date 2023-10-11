from flask_login import current_user
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from werkzeug.security import generate_password_hash

from config import *
from forms import forms
from forms.forms import RegistrationForm

"""
Load a user from the database based on the given user ID.

Parameters:
    user_id (int): The ID of the user to load.

Returns:
    User: The user object corresponding to the given ID.
"""


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(Base, db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_authenticated: Mapped[bool] = mapped_column(Boolean, default=False)
    is_anonymous: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'


"""
Function for handling the '/signup' route. 

Parameters:
    None

Returns:
    If the request method is 'GET':
        - Renders the 'signup.html' template with the RegistrationForm object.
    If the request method is 'POST':
        - Creates a new User object with the username, email, and password 
          obtained from the request form.
        - Checks if the passwords entered by the user match. If they don't, 
          displays a flash message and redirects to the 'signup.html' template.
        - Commits the new User object to the database.
        - Attempts to log in the user and prints a success message.
        - If an exception occurs during the login process, prints an error 
          message and redirects to the 'signup' route.
        - Redirects to the 'profile' route.

"""


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hash_password = generate_password_hash(request.form['password'], "sha256")
        confirm = request.form["confirm"]
        user = User(
            username=username,
            email=email,
            password=hash_password,
            is_active=True,
            is_authenticated=True,
            is_anonymous=False,
        )

        # Vérifier que les mots de passe sont identiques
        if password != confirm:
            flash('Les mots de passe ne correspondent pas.', "connection_failed")
            return render_template('signup.html', form=form)
        else:
            # Enregistrer l'utilisateur
            db.session.add(user)
            db.session.commit()

        try:
            login_user(user)
            print('Inscription réussie et connexion effectuée.')
        except Exception as e:
            print("Erreur d'authentification:" + str(e))
            redirect(url_for('signup'))

        return redirect(url_for('profile'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.Login_form()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Identifiants incorrects.', "connection_failed")
            return render_template('login.html', form=form)
        try:
            login_user(user)
            print('Connexion effectuée.')
            return redirect(url_for('profile'))
        except Exception as e:
            print("Erreur d'authentification:" + str(e))
            flash(f"Erreur d'authentification : {str(e)}", "connection_failed")
    return render_template('login.html', form=form)


"""
Log out the current user and redirect to the login page.

Parameters:
    None

Returns:
    flask.Response: A redirect response to the login page.
"""


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


"""
Render the profile page.

This function is responsible for rendering the profile page. It is accessible through the '/profile' endpoint 
and supports both GET and POST requests. The function requires the user to be logged in, as indicated by the @login_required decorator.

Parameters:
    None

Returns:
    A rendered profile.html template with the 'user' variable set to the current logged-in user.

"""


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)


"""
A function that serves as the handler for the home route.

Returns:
    The rendered HTML template for the index page.
"""


@app.route('/')
def home():
    return render_template('index.html')


"""
Error handler for internal server errors.

Args:
    error (Exception): The exception that caused the internal server error.

Returns:
    tuple: A tuple containing the error message and the HTTP status code.

"""


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500


if __name__ == '__main__':
    app.run(debug=True)
