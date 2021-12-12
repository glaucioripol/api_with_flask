from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import Configuration

Base = declarative_base()

db_engine = create_engine(Configuration.db_string_connection)
