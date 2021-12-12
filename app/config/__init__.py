from os import getenv

from dotenv import load_dotenv
load_dotenv()


class Configuration:
    is_dev: bool = getenv('IS_DEV') == '1'

    # JWT
    jwt_secret: str = getenv('JWT_SECRET')
    jwt_issuer: str = getenv('JWT_ISSUER')
    jwt_authtype: str = getenv('JWT_AUTHTYPE')

    # Database
    db_string_connection: str = getenv('DB_STRING_CONNECTION')
