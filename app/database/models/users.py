from sqlalchemy.sql.expression import null
from app.database import database


class UsersModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(120), nullable=False)
    password = database.Column(database.String(120), nullable=False)

    def __repr__(self):
        return f'User {self.name}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password
        }
