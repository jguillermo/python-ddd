import unittest
from unittest import mock

from sdk.types import TypeUuid
from src.user import UserCreateUseCase
from src.user.application.use_cases.user import UserCreateInput
from src.user.domain.user import UserRepository


class UserMockRepository:

    @staticmethod
    def mng_ok():
        repository = mock.create_autospec(UserRepository)
        repository.persist.return_value = True
        return repository


class TestUserCreateService(unittest.TestCase):

    def test_user_create_ok(self):
        service = UserCreateUseCase(UserMockRepository.mng_ok())

        id = TypeUuid.random().value()
        user_create_input = UserCreateInput(
            id=id,
            name='jose',
            last_name='Guillermo'
        )
        status=service.execute(user_create_input)
        self.assertEqual(True, status)





