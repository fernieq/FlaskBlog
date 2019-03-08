from flask import Flask
#import different classes from flask extension
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


#initiate flask database instance
db = SQLAlchemy()
#initiate flask bcrypt instance
bcrypt = Bcrypt()
#initiate flask login manager instance
login_manager = LoginManager()

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
#initiate flask mail instance
mail = Mail()

def create_app(config_class=Config):
    #creation of the app instance 
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
