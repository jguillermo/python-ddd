from abc import ABC, abstractmethod


# class Message(ABC):
#     def __init__(self) -> None:
#         self._message_id = 1234
#
#     def message_id(self):
#         return self._message_id
#
#     @abstractmethod
#     def message_type(self):
#         pass


class Request(ABC):
    def request_id(self):
        return 1234

    @abstractmethod
    def message_type(self):
        pass


class Command(Request):

    def command_id(self):
        return self.request_id()

    def message_type(self):
        return 'command'


class CommandBus(ABC):

    def _guard(self, command):
        if not isinstance(command, Command):
            raise HandlerTypeError("Debe ser de tipo Command")

    @abstractmethod
    def dispatch(self, command: Command):
        pass

    # @abstractmethod
    # def register(self, command_class, handler):
    #     pass


class Query(Request):
    def message_type(self):
        return 'query'


class QueryBus(ABC):
    def _guard(self, command):
        if not isinstance(command, Query):
            raise HandlerTypeError("Debe ser de tipo Query")

    @abstractmethod
    def ask(self, query: Query):
        pass

    # @abstractmethod
    # def register(self, query_class, handler):
    #     pass


class HandlerNotFound(Exception):
    pass


class HandlerTypeError(Exception):
    pass


class Handler(ABC):
    @abstractmethod
    def handle(self, command):
        pass
