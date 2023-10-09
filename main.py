from flask_login import current_user
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from werkzeug.security import generate_password_hash
from forms.forms import RegistrationForm, Todo_Form
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


@login_manager.user_loader
def load_user(user_id):
    def __init__(self, username, email, password):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password


class User(Base, UserMixin):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


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
            login_user(user, force=True)
            if user.is_authenticated:
                redirect(url_for('index'))
            else:
                redirect(url_for('signup'))

            print('Inscription réussie et connexion effectuée.')
        except Exception as e:
            flash('Erreur de connexion.', "login_failed")
            print("Erreur d'authentification:" + str(e))
            redirect(url_for('signup'))

        return redirect(url_for('profile'))
    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/profile', methods=['GET', 'POST'])
#@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500


app.run(debug=True)
