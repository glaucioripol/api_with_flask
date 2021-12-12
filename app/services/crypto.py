from bcrypt import gensalt, hashpw, checkpw


class CryptoPassword:
    @staticmethod
    def hash_password(password: str):
        return hashpw(
            password.encode('utf-8'),
            gensalt(14)
        )

    @staticmethod
    def check_password(password: str, hashed_password: bytes):
        return checkpw(
            password.encode('utf-8'),
            hashed_password
        )
