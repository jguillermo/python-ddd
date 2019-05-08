# -*- coding: utf-8 -*-
import falcon

from bootstrap.framework.decorators.service import handler_except


class Base:

    def __init__(self) -> None:
        pass
        # self.command_bus = CommandBusSync()
        # self.query_bus = QueryBusSync()

    def print(self, value):
        print('*****************************')
        print(value)
        print('--*************************--')

    def data_token(self, req: falcon.Request):
        return req.get_param('app_data_token')

    def user_id_token(self, req: falcon.Request):
        data_token = self.data_token(req)
        return data_token['id']

    def is_user_admin_token(self, req: falcon.Request):
        data_token = self.data_token(req)
        return data_token['role'] == 'admin'
