import unittest
from unittest import mock

from sdk.adapter.event import Event
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


class EventMock:

    @staticmethod
    def url():
        event = mock.create_autospec(Event)
        event.publish.return_value = True
        return event


class TestUserCreateService(unittest.TestCase):

    def test_user_create_ok(self):
        service = UserCreateUseCase(UserMockRepository.mng_ok(), EventMock.url())

        id = TypeUuid.random().value()
        user_create_input = UserCreateInput(
            id=id,
            name='jose',
            last_name='Guillermo'
        )
        status = service.execute(user_create_input)
        self.assertEqual(True, status)
