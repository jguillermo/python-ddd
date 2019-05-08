import inspect
from abc import ABC, abstractmethod


class HandlerNotFound(Exception):
    pass


class Resolver:

    def handler_for(self, command):
        try:
            print(command.__class__.__name__ + 'Handler')
            print(getattr(self._getmodule(command), command.__class__.__name__ + 'Handler'))
            return getattr(self._getmodule(command), command.__class__.__name__ + 'Handler')
        except AttributeError:
            return None

    def _getmodule(self, command):
        print(inspect.getmodule(command))
        return inspect.getmodule(command)


class Bus:
    resolver = None

    def __init__(self, resolver=None):
        self.resolver = resolver or Resolver()

    def execute(self, command):
        handler_cls = self.resolver.handler_for(command)
        if handler_cls is None:
            raise HandlerNotFound('Unable to find handler for ' + command.__class__.__name__)
        return handler_cls().handle(command)


class SayHelloCommand:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SayHelloCommandHandler:

    def handle(self, command):
        print("Hello, " + command.name)


class Handler(ABC):

    @abstractmethod
    def handle(self, command):
        pass
