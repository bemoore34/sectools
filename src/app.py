from flask import Flask, render_template
from src.common.database import Database
from src.models.users.views import user_blueprint

__author__ = 'bmoore'

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "cqw89asdg8f7swKjb34r89RGesf89345KLH%s;lJWhfewgoYi3q4?f034fojir!eWg$f90q/ewrgf"
# This secret key is used to secure Flask sessions, which use session cookies and other data that we can
# pass, like email. The secret is used to encrypt the session cookies that Flask uses to manage sessions.
# We will create a routine for generating a secure key and we want to do this every time the application
# is started - should not be hard coded.


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.jinja2')


app.register_blueprint(user_blueprint, url_prefix="/users")