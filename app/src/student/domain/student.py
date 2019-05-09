from abc import ABC, abstractmethod


class Student:
    def __init__(self, id, name, last_name) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.code = 'sdf'


class StudentRepository(ABC):

    @abstractmethod
    def persist(self, student: Student):
        pass

    @abstractmethod
    def find_by_id(self, student_id: str) -> Student:
        pass

    @abstractmethod
    def list_all(self):
        pass
