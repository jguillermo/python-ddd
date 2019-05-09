from sqlalchemy.orm import clear_mappers
from sqlalchemy import MetaData

from src.student.infrastructure.repository.sqlalchemy.mapping import load_mapper_student
from src.user.infrastructure.repository.sqlalchemy.mapping import load_mapper_user

metadata_app = MetaData()
clear_mappers()
load_mapper_user(metadata_app)
load_mapper_student(metadata_app)


def load_mapper_app():
    print("inicio el mapper!!!!!!!!!!!!")
