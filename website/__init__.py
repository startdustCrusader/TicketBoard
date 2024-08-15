'''
    ** This file is the init file used to initialise the application
    ** Used to register blueprint, and login utility
'''

#import Requirements
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database1.db'

#initialize Flask and adding SQL Alchemy
#Intialize the app

#Main Application 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomABC89897123123871937917'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #assign our app to Flask


    from .views import views #Main ticket homePage
    from .auth import auth    #All Login-LogOut Page
    #importing from the two views

    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')
    
    #importing DB model
    from .models import User, Ticket #importing database-class objects 
    with app.app_context():
        db.create_all()

    #Login manager and Auth
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

