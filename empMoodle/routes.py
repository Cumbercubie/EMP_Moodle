from flask import Blueprint,render_template,url_for,flash,redirect
from empMoodle import app,db
from empMoodle.forms import LoginForm, RegistrationForm



# auth = Blueprint('auth',__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('login.html')
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('properlogin.html',title="Login",form=form)

@app.route('/logout')
def logout():
    return 'Logout'
