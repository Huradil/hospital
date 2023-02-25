from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

app=Flask(__name__)
db=SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
app.config['SECRET_KEY']='secret_key'
db.init_app(app)

migrate=Migrate(app,db)

# login_manager=LoginManager(app)
# bcrypt=Bcrypt(app)

from .urls import *