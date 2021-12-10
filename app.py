# dotenv needs be on top of the imports
from dotenv import load_dotenv
load_dotenv()


from app.resources.users import Users
from app.server import app, api
from os import getenv


api.add_resource(Users, "/user")

# # Run the application
if __name__ == "__main__":
    if getenv('IS_DEV') == '1':
        app.run(debug=True, port=3333)
    else:
        app.run(debug=False, port=3333, host='0.0.0.0')
