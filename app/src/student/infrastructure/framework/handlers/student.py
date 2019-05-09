# -*- coding: utf-8 -*-
import falcon

from bootstrap.framework.decorators.service import handler_except
from bootstrap.framework.handlers import Base
from src.student import StudentUseCaseDI


class StudentHandler(Base):

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        return StudentUseCaseDI.student_list().execute()
