from flask_pyjwt import AuthManager, current_token, require_token
from app.server import app


auth_manager = AuthManager(app)


class jwt_services:
    @staticmethod
    def require_auth_token():
        return require_token('auth')

    @staticmethod
    def get_jwt_manager():
        return auth_manager

    @staticmethod
    def generate_auth_token(data):
        return auth_manager.auth_token(data).signed

    @staticmethod
    def get_jwt_value():
        return current_token.sub
