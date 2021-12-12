from app.server import app
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy(app)
session_database = database.session

metadata = database.metadata


def get_engine():
    return database.engine
