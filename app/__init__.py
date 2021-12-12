from flask_migrate import Migrate

from app.server import app, api
from app.database import database
from app.resources.users import Users


api.add_resource(Users, "/user")

migrate = Migrate(app, database)


def create_app():
    migrate.init_app(app, database)
    return app
