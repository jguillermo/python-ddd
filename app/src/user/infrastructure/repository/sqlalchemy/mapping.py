from sqlalchemy import Table, Column, String, CHAR, Boolean, Text, SmallInteger, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapper, relationship

from src.user.domain.user import User


def load_mapper_user(metadata_app):
    user = Table('reto_user', metadata_app,
                 Column('id', CHAR(36), primary_key=True),
                 Column('name', String(200), nullable=True),
                 Column('last_name', String(200), nullable=True)
                 )
    mapper(User, user)
