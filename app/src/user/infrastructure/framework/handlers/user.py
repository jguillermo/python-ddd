# -*- coding: utf-8 -*-
import falcon

from bootstrap.framework.decorators.service import handler_except
from bootstrap.framework.handlers import Base
from sdk.types import TypeUuid
from src.user import UserUseCaseDI
from src.user.application.use_cases.user import UserCreateInput, UserEditInput


class UserHandler(Base):

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        id = TypeUuid.random().value()
        user_create_input = UserCreateInput(
            id=id,
            name=req.media.get('name'),
            last_name=req.media.get('last_name')
        )
        UserUseCaseDI.user_create().execute(user_create_input)
        return {'id': id}

    @handler_except
    def on_put(self, req: falcon.Request, resp: falcon.Response):
        user_update_input = UserEditInput(
            id=req.media.get('id'),
            name=req.media.get('name'),
            last_name=req.media.get('last_name')
        )
        UserUseCaseDI.user_update().execute(user_update_input)
        return 'ok'

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        return UserUseCaseDI.user_list().execute()
