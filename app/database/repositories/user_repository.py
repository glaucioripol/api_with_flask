from models import UsersModel


class UserRepository:
    def __init__(self) -> None:
        self.model = UsersModel()

    def get_by(self, created_at: str, updated_at: str, search_by: str = None) -> list:
        self.model.query.filter(UsersModel.created_at.startswith(
            created_at), UsersModel.updated_at.startswith(updated_at))
        if search_by:
            self.model.query.filter(UsersModel.name.contains(search_by))
        return self.model.query.all()
