
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from src.user.domain.user import UserRepository, User


class UserSqlAlchemyRepository(UserRepository):

    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter._entity = User

    def persist(self, user: User):
        return self.__adapter.persist(user)

    def find_by_id(self, user_id: str) -> User:
        return self.__adapter.find_by_id(user_id)

    def list_all(self):
        sql = "select * from reto_user"
        return self.__adapter.result(sql)
