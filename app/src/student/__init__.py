# -*- coding: utf-8 -*-

from bootstrap.container import AdapterSqlAlchemyDI
from src.student.application.use_cases.student import StudentCreateUseCase, StudentUpdateUseCase, StudentListUseCase
from src.student.infrastructure.repository.sqlalchemy.student_alchemy_repository import StudentSqlAlchemyRepository


class StudentRepositoryDI:
    """
        Repository
    """
    @staticmethod
    def student_repository():
        return StudentSqlAlchemyRepository(adapter=AdapterSqlAlchemyDI.orm())

class StudentUseCaseDI:
    """
        Use Cases
    """
    @staticmethod
    def student_create():
        return StudentCreateUseCase(student_repository=StudentRepositoryDI.student_repository())

    @staticmethod
    def student_update():
        return StudentUpdateUseCase(student_repository=StudentRepositoryDI.student_repository())

    @staticmethod
    def student_list():
        return StudentListUseCase(student_repository=StudentRepositoryDI.student_repository())

