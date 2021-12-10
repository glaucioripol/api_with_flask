from os import getenv
from flask import Flask
from flask_restful import Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


app.config["JWT_ISSUER"] = getenv("JWT_ISSUER")
app.config["JWT_AUTHTYPE"] = getenv('JWT_AUTHTYPE')
app.config["JWT_SECRET"] = getenv('JWT_SECRET')
app.config["JWT_AUTHMAXAGE"] = 3600
app.config["JWT_REFRESHMAXAGE"] = 604800
