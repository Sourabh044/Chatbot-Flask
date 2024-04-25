from dotenv import load_dotenv
import os


load_dotenv()


DB_URI = os.environ.get('DB_URI')
APP_SECRET = os.environ.get('APP_SECRET')
