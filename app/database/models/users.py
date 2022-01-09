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
    created_at = database.Column(
        database.DateTime,
        nullable=False,
        default=database.func.now()
    )
    updated_at = database.Column(
        database.DateTime,
        nullable=False,
        default=database.func.now(),
        onuppoate=database.func.now()
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'spends': [spend.to_dict() for spend in self.spends],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
