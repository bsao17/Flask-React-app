import os

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from werkzeug.security import generate_password_hash
import dotenv

from models import *


class Base(DeclarativeBase):
    pass


load_dotenv(dotenv_path=".flaskenv")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
login_manager.init_app(app=app)
db.init_app(app)
CORS(app)
with app.app_context():
    db.create_all()


class Todo_Form(FlaskForm):
    user = StringField(validators=[InputRequired(), Length(min=1, max=50)])
    date = DateField('Date', format='%d-%m-%Y')
    task = TextAreaField(validators=[InputRequired(), Length(max=200)])
    closed = BooleanField('Available', default='checked')


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.Length(min=4),
        validators.equal_to('confirm', message="Passwords must match")
    ])
    confirm = PasswordField('Repeat Password')
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])


@login_manager.request_loader
def load_user(user_id):
    def __init__(self, username, email, password):
        self.id = user_id
        self.username = username
        self.email = email
        self.password = password


class User(Base):
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
        password_confirm = generate_password_hash(request.form['confirm'], "sha256")

        # Enregistrer l'utilisateur
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('signup.html', form=form)

        # Vérifier que les mots de passe sont identiques
        # if password != password_confirm:
        #     flash('Les mots de passe ne correspondent pas.')
        #     return render_template('signup.html', form=form)
        #
        # Vérifier si l'utilisateur existe déjà
        # existing_user = User.query.filter_by(username=username).first()
        # if existing_user:
        #     flash('Ce nom d\'utilisateur est déjà pris.')
        #     return# render_template('signup.html', form=form)
        #
        # hashed_password = generate_password_hash(password, method='sha256')
        #
        # Confirmer l'authentification
        # login_user(new_user)
        #
        # flash('Inscription réussie et connexion effectuée.')
        # return redirect(url_for('home'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile():
    return render_template('profile.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500


app.run(debug=True)
