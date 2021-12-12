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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'owner_id': self.owner_id
        }
