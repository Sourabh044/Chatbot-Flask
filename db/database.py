from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import configure_mappers
db: SQLAlchemy = SQLAlchemy()
configure_mappers()
