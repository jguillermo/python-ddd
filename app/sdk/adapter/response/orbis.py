# -*- coding: utf-8 -*-


class Response(object):
    PROCESS_SUCCESS_CODE = 2000
    PROCESS_SUCCESS_MESSAGE = 'SUCCESS'
    PROCESS_ERROR_CODE = 4000
    PROCESS_ERROR_MESSAGE = 'ERROR'

    def success(self, data):
        try:
            return self._schema(False,
                                self.PROCESS_SUCCESS_CODE,
                                self.PROCESS_SUCCESS_MESSAGE,
                                data if data is not None else [])
        except Exception as e:
            raise e

    def error(self, message, code=None):
        try:
            return self._schema(True,
                                self.PROCESS_ERROR_CODE if code is None else code,
                                self.PROCESS_ERROR_MESSAGE if message is None else message,
                                [])
        except Exception as e:
            raise e

    @staticmethod
    def _schema(error, code, message, data):
        return {
            'error': error,
            'code': code,
            'message': message,
            'data': data
        }
