from abc import ABC, abstractmethod


class User:
    def __init__(self, id, name, last_name) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name


class UserRepository(ABC):

    @abstractmethod
    def persist(self, user: User):
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def list_all(self):
        pass
