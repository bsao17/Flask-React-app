from flask_login import current_user
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from werkzeug.security import generate_password_hash
from forms.forms import RegistrationForm
from config import *

load_dotenv(dotenv_path=".flaskenv")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app=app)

CORS(app)

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


class User(Base, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None

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
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=generate_password_hash(request.form['password'], "sha256")
        )

        # Vérifier que les mots de passe sont identiques
        if request.form['password'] != request.form['confirm']:
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


app.run(debug=True)
