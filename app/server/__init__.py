from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.config import Configuration

app = Flask(__name__)
api = Api(app)
CORS(app)

# JWT
app.config["JWT_ISSUER"] = Configuration.jwt_issuer
app.config["JWT_AUTHTYPE"] = Configuration.jwt_authtype
app.config["JWT_SECRET"] = Configuration.jwt_secret
app.config["JWT_AUTHMAXAGE"] = 3600
app.config["JWT_REFRESHMAXAGE"] = 604800

# database
app.config["SQLALCHEMY_DATABASE_URI"] = Configuration.db_string_connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
