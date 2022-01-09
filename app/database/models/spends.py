from app.database import database


class SpendsModel(database.Model):
    __tablename__ = 'spends'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(120), nullable=False)
    value = database.Column(database.Float, nullable=False)
    owner_id = database.Column(
        database.Integer,
        database.ForeignKey('users.id'),
        nullable=False
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
        onupdate=database.func.now()
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
