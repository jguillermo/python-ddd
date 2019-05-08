# -*- coding: utf-8 -*-

from bootstrap.container import AdapterSqlAlchemyDI
from src.user.application.use_cases.user import UserCreateUseCase, UserUpdateUseCase, UserListUseCase
from src.user.infrastructure.repository.sqlalchemy.user_alchemy_repository import UserSqlAlchemyRepository


class UserRepositoryDI:
    """
        Repository
    """
    @staticmethod
    def user_repository():
        return UserSqlAlchemyRepository(adapter=AdapterSqlAlchemyDI.orm())

class UserUseCaseDI:
    """
        Use Cases
    """
    @staticmethod
    def user_create():
        return UserCreateUseCase(user_repository=UserRepositoryDI.user_repository())

    @staticmethod
    def user_update():
        return UserUpdateUseCase(user_repository=UserRepositoryDI.user_repository())

    @staticmethod
    def user_list():
        return UserListUseCase(user_repository=UserRepositoryDI.user_repository())

