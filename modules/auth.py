from flask_login import LoginManager
from db import User
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from db import db

migrate = Migrate()
bcrypt = Bcrypt()

'''Setting up the flask_login module'''
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

# This function is a user loader for Flask-Login, used to reload the user
# object from the user ID stored in the session.


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)
    # return User.query.get(int(user_id))
