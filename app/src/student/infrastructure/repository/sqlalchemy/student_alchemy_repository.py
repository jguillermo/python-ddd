
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from src.student.domain.student import StudentRepository, Student


class StudentSqlAlchemyRepository(StudentRepository):

    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter._entity = Student

    def persist(self, student: Student):
        return self.__adapter.persist(student)

    def find_by_id(self, student_id: str) -> Student:
        return self.__adapter.find_by_id(student_id)

    def list_all(self):
        sql = "select * from reto_student"
        return self.__adapter.result(sql)
