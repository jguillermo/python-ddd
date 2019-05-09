from sdk.exception import BadRequest
from src.student.domain.student import StudentRepository, Student


class StudentCreateInput:
    def __init__(self, id, name, last_name) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name


class StudentEditInput(StudentCreateInput):
    pass


class StudentCreateUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self.student_repository = student_repository

    def execute(self, input: StudentCreateInput):
        student = Student(input.id, input.name, input.last_name)
        return self.student_repository.persist(student)


class StudentUpdateUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self.student_repository = student_repository

    def execute(self, input: StudentEditInput):
        student = self.student_repository.find_by_id(input.id)
        if student is None:
            raise BadRequest("no existe el usuario")
        student.name = input.name
        student.last_name = input.last_name
        self.student_repository.persist(student)


class StudentListUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self.student_repository = student_repository

    def execute(self):
        return self.student_repository.list_all()
