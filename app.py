from app.config import Configuration
from app.server import app, api
from app.resources.users import Users


api.add_resource(Users, "/user")

# # Run the application
if __name__ == "__main__":
    if Configuration.is_dev:
        app.run(debug=True, port=3333)
    else:
        app.run(debug=False, port=3333, host='0.0.0.0')
