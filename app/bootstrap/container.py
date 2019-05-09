# -*- coding: utf-8 -*-
from bootstrap.config import FileConfig
from sdk.adapter.encryption.jwt import JwtEncrypt
from sdk.adapter.event.aws import ApiWateway
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter, SqlAlchemySession


class ConfigDI:
    @staticmethod
    def file():
        return FileConfig()

class AdapterSqlAlchemyDI:
    @staticmethod
    def alchemy_session():
        return SqlAlchemySession(config=ConfigDI.file())

    @staticmethod
    def orm():
        return SqlAlchemyAdapter(sql_alchemy_session=AdapterSqlAlchemyDI.alchemy_session())

class EncryptDI:
    @staticmethod
    def jwt():
        return JwtEncrypt()

class EventAdapterDI:
    @staticmethod
    def aws_url():
        return ApiWateway(config=ConfigDI.file())


