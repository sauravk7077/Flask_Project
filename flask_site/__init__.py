from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os, socket


#socket.getaddrinfo('localhost', 5000)
app = Flask(__name__)


# To import the secret key
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


#These are configuration for mail servies
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD']= os.getenv('EMAIL_PASS')
mail = Mail(app=app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category= 'info'

from flask_site.users.routes import users
from flask_site.posts.routes import posts
from flask_site.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)