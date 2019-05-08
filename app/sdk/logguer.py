import datetime
from abc import ABC, abstractmethod

from bootstrap.container import AdapterSqlAlchemyDI
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from sdk.types import TypeUuid
from sdk.automation import Singleton


class LogguerData(metaclass=Singleton):
    body=''


class LogguerApp(ABC):
    @abstractmethod
    def service(self, service_name, user_id, param1):
        pass


class LoggerAppEntity:
    def __init__(self, id, service_name, user_id, param):
        data = LogguerData()

        self.id = id
        self.service_name = service_name
        self.user_id = user_id
        self.param = param
        self.platform= data.body
        self.created_at = datetime.datetime.now()


class LogguerAppSql(LogguerApp):

    def service(self, service_name, user_id, param):
        adapter = SqlAlchemyAdapter(AdapterSqlAlchemyDI.alchemy_session())
        id = TypeUuid.random().value()
        logger_app_entity = LoggerAppEntity(id, service_name, user_id, param)
        adapter.persist(logger_app_entity)



class LogguerAppCmd(LogguerApp):
    def service(self, service_name, user_id, param1: None):
        print('-' * 50)
        print('service name : ', service_name)
        print('user id : ', user_id)
        print('parmas : ', param1)
        print('-' * 50)
