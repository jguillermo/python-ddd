# -*- coding: utf-8 -*-
import falcon
from functools import wraps

from sdk.adapter.log.logging import ConsoleLogger
from sdk.adapter.response.orbis import Response
from sdk.exception import BadRequest, UnauthorizedRequest
from sdk.logguer import LogguerData

response = Response()


def handler_except(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        req = args[1]  # type: falcon.Request
        resp = args[2]  # type: falcon.Response
        try:
            data = LogguerData()
            data.body = req.get_header('Platform', default='')

            rpta = method(*args, **kwargs)
            resp.media = response.success(rpta)
            resp.status = falcon.HTTP_200
        except UnauthorizedRequest as ua:
            resp.media = response.error(ua.__str__(), 4001)
            resp.status = falcon.HTTP_401
        except BadRequest as br:
            resp.media = response.error(br.__str__())
            resp.status = falcon.HTTP_400
        except Exception as e:
            logger = ConsoleLogger()
            #logger.output.error('=== Handler exception ===')
            logger.output.error(str(e), exc_info=True)
            #logger.output.error('=' * 25)
            resp.media = response.error(e.__str__())
            resp.status = falcon.HTTP_500

    return method_wrapper
