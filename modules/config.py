from dotenv import load_dotenv
import os


load_dotenv()


class Development(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
    SECRET_KEY = os.environ.get('APP_SECRET')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'superhero'
