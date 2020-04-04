from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY']='ff8b45d8b7d5cb5905c479e6ae1b137d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category = 'card-panel blue-text text-darken-1'
from empMoodle import routes