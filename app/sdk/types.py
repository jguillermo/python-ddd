import uuid
from abc import ABC, abstractmethod

from sdk.exception import BadRequest


class TypeBase():

    def __init__(self, value, is_required: bool):
        self._is_required = is_required
        self._value = value

    def is_required(self):
        return self._is_required

    def validate(self, value_name=''):
        text = 'parámetro' if value_name == '' else value_name
        if self.is_required() and self._value is None:
            raise BadRequest("El {} es requerido".format(text))

    def value(self):
        return self._value

    def is_not_none(self) -> bool:
        return self._value is not None


class TypeString(TypeBase):

    def __init__(self, value: str, is_required: bool = True):
        super().__init__(value, is_required)

    def validate(self, value_name=''):
        super().validate(value_name)
        if self.is_not_none() and not isinstance(self._value, str):
            raise BadRequest("El tipo de dato no es un string {}".format(self._value))

    def value(self) -> str:
        return super().value()

    def __str__(self) -> str:
        return self.value()


# @staticmethod
# def create(value):
#     string = self(value)
#     string.validate()
#     return string


class TypeUuid(TypeString):
    def __init__(self, value: str):
        super().__init__(value, True)

    @staticmethod
    def random():
        return TypeUuid(uuid.uuid4().__str__())

    @staticmethod
    def by_name(name: str):
        return TypeUuid(uuid.uuid5(uuid.NAMESPACE_DNS, name).__str__())

    def validate(self, value_name=''):
        super().validate(value_name)
        # aqui va una validacion de uuid
        return True


class TypeInteger(TypeBase):

    def __init__(self, value: int, is_required: bool = True):
        super().__init__(value, is_required)

    def validate(self, value_name=''):
        super().validate(value_name)
        if self.is_required() and not isinstance(self._value, int):
            raise BadRequest('El tipo de dato no es un integer')

    def value(self) -> int:
        return super().value()
