from .user_repository import UserRepository


class TestUserRepository(UserRepository):
    def __init__(self) -> None:
        self.model = UserRepository()
        self.users = [
            {
                "id": 1,
                "username": "test_user_repository",
                "email": "",
                "password": "",
                "status": "",
                "created_at": "",
                "updated_at": "",
            }
        ]

    def test_get_by(self, created_at: str, updated_at: str, search_by: str = None) -> list:
        doido = self.model.get_by(created_at, updated_at, search_by)
        print(doido)
