from flask import Blueprint,render_template,url_for,flash,redirect, request
from empMoodle import app,db, login_manager
from empMoodle.forms import LoginForm, RegistrationForm
from empMoodle.models import User
from flask_login import login_user, current_user, logout_user,login_required

# auth = Blueprint('auth',__name__)

@app.route('/')
@login_required
def index():
    
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method=='POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and form.password.data==user.password:
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('index'))
            flash('Login Unsuccessfull. Please check username and password','red')
                # return redirect(url_for('index'))
        else:
            print(form.errors)
    
    return render_template('properlogin.html',title="Login",form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
