from app.server import app
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy(app)
session_database = database.session
