# -*- coding: utf-8 -*-
import falcon

from bootstrap.framework.decorators.service import handler_except
from bootstrap.framework.handlers import Base
from sdk.types import TypeUuid
from src.student import StudentUseCaseDI
from src.student.application.use_cases.student import StudentCreateInput, StudentEditInput


class StudentHandler(Base):

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        id = TypeUuid.random().value()
        student_create_input = StudentCreateInput(
            id=id,
            name=req.media.get('name'),
            last_name=req.media.get('last_name')
        )
        StudentUseCaseDI.student_create().execute(student_create_input)
        return {'id': id}

    @handler_except
    def on_put(self, req: falcon.Request, resp: falcon.Response):
        student_update_input = StudentEditInput(
            id=req.media.get('id'),
            name=req.media.get('name'),
            last_name=req.media.get('last_name')
        )
        StudentUseCaseDI.student_update().execute(student_update_input)
        return 'ok'

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        return StudentUseCaseDI.student_list().execute()
