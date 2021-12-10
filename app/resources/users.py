from flask_restful import Resource, request
from app.services.jwt import jwt_services


class Users(Resource):
    @jwt_services.require_auth_token()
    def get(self):
        return {
            "token_data": jwt_services.get_jwt_value(),
        }

    def post(self):
        request_data = request.get_json()
        auth_token = jwt_services.generate_auth_token(request_data)
        return {
            "token": auth_token
        }
