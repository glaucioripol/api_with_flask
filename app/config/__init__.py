from os import getenv

from dotenv import load_dotenv
load_dotenv()


def get_corret_db_string_connection():
    if getenv('IS_DEV') == '1':
        return getenv('DB_STRING_CONNECTION_DEV')
    else:
        return getenv('DB_STRING_CONNECTION_PROD')


class Configuration:
    is_dev: bool = getenv('IS_DEV') == '1'

    # JWT
    jwt_secret: str = getenv('JWT_SECRET')
    jwt_issuer: str = getenv('JWT_ISSUER')
    jwt_authtype: str = getenv('JWT_AUTHTYPE')

    # Database
    db_string_connection: str = get_corret_db_string_connection()
