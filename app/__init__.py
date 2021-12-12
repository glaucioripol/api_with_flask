from flask_migrate import Migrate

from app.server import app, api
from app.database import database
from app.resources.users import Users
from app.database.models import *


api.add_resource(Users, "/user")

migrate = Migrate(app, database)


def create_app():
    migrate.init_app(app, database)
    return app

# # Run the application
# if __name__ == "__main__":
#     if Configuration.is_dev:
#         app.run(debug=True, port=3333)
#     else:
#         app.run(debug=False, port=3333, host='0.0.0.0')
