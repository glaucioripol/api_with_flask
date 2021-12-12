from app.database import database


class UsersModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(120), nullable=False)
    password = database.Column(database.String(120), nullable=False)
    email = database.Column(database.String(120), nullable=False)
    spends = database.relationship(
        'spends',
        backref='users',
        lazy=True
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'spends': [spend.to_dict() for spend in self.spends]
        }
