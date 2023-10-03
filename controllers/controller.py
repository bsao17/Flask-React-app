from models import *

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
CORS(app)


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
        validators.Length(min=8),
        validators.equal_to('confirm', message="Passwords must match")
    ])
    confirm = PasswordField('Repeat Password')
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])


login_manager = LoginManager()
login_manager.init_app(app=app)


@login_manager.request_loader
def load_user(user_id):
    return user_id


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(request.form['email'])
        password = User(request.form['password'])
        print(request.form['email'])
        login_user(user)
        flash('Logged in successfully.')
        return redirect(url_for('profile'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SELECT * FROM `acn_blog`.`tasks` LIMIT 1000;")
    return [data]


@app.route('/database')
def database():
    data = Database('localhost', 'acn_blog', 'root', 'root').query("SELECT * FROM `acn_blog`.`users` LIMIT 1000;")
    return [data]


@app.errorhandler(500)
def internal_server_error(error):
    return "Erreur interne du serveur", 500
