from sqlalchemy import Table, Column, String, CHAR, Boolean, Text, SmallInteger, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapper, relationship

from src.student.domain.student import Student


def load_mapper_student(metadata_app):
    student = Table('reto_student', metadata_app,
                 Column('id', CHAR(36), primary_key=True),
                 Column('name', String(200), nullable=True),
                 Column('last_name', String(200), nullable=True)
                 )
    mapper(Student, student)
