from sdk.exception import BadRequest
from sdk.filter import Filter



class Process:
    @staticmethod
    def integer(value, label=''):

        value = Filter.integer(value)

        if value is None:
            raise BadRequest('{} es requerido'.format(label).strip())

        if not isinstance(value, int):
            raise BadRequest('{} debe ser un número entero'.format(label).strip())

        return value

    @staticmethod
    def string(value, label=''):

        value = Filter.integer(value)

        if value is None:
            raise BadRequest('{} es requerido'.format(label).strip())

        if not isinstance(value, str):
            raise BadRequest('{} debe ser un string'.format(label).strip())

        return value
