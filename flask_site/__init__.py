from flask import Flask, render_template, url_for, flash, redirect

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)


# To import the secret key
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
