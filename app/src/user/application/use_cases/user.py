from sdk.exception import BadRequest
from src.user.domain.user import UserRepository, User


class UserCreateInput:
    def __init__(self, id, name, last_name) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name


class UserEditInput(UserCreateInput):
    pass


class UserCreateUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, input: UserCreateInput):
        user = User(input.id, input.name, input.last_name)
        return self.user_repository.persist(user)


class UserUpdateUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, input: UserEditInput):
        user = self.user_repository.find_by_id(input.id)
        if user is None:
            raise BadRequest("no existe el usuario")
        user.name = input.name
        user.last_name = input.last_name
        self.user_repository.persist(user)


class UserListUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.list_all()
