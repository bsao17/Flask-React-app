import os
from werkzeug.security import generate_password_hash
import dotenv

from models import *

load_dotenv(dotenv_path=".flaskenv")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
print(f"SQLALCHEMY_DATABASE_CONNECT = {os.getenv('SQLALCHEMY_DATABASE_CONNECT')}")
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
    pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        # Vérifier que les mots de passe sont identiques
        if password != password_confirm:
            flash('Les mots de passe ne correspondent pas.')
            return render_template('login.html', form=form)

        # Vérifier si l'utilisateur existe déjà
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Ce nom d\'utilisateur est déjà pris.')
            return render_template('login.html', form=form)

        # Créer le nouvel utilisateur
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Confirmer l'authentification
        login_user(new_user)

        flash('Inscription réussie et connexion effectuée.')
        return redirect(url_for('profile.html'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    stmt = "SELECT * FROM tasks"
    result = db.session.execute(text(stmt))
    all_tasks = []
    for task in result:
        all_tasks.append({'id': task[0], 'name': task[1], 'task_date': task[2], 'task': task[3], 'closed': task[4]})
    return {'tasks': all_tasks}


@app.route('/users')
def database():
    stmt = text('SELECT * FROM users')
    result = db.session.execute(stmt)
    users = []
    for row in result:
        users.append({'id': row[0], 'username': row[1], 'email': row[2],
                      'password': "prohibited"})
    return {'users': users}


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500


if __name__ == '__main__':
    app.run(debug=True)
