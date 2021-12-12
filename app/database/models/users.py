from . import Base
from sqlalchemy import Column, Integer, String


class UsersModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.name}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password
        }
