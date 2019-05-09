import falcon

from bootstrap.framework.decorators.service import handler_except
from bootstrap.framework.handlers import Base
from src.student import StudentUseCaseDI
from src.student.application.use_cases.student import StudentCreateInput, StudentEditInput


def app_user_create_end(attributes, transaction_id):
    student_create_input = StudentCreateInput(
        id=attributes['id'],
        name=attributes['name'],
        last_name=attributes['last_name']
    )
    StudentUseCaseDI.student_create().execute(student_create_input, transaction_id)


def app_user_update_end(attributes, transaction_id):
    student_update_input = StudentEditInput(
        id=attributes['id'],
        name=attributes['name'],
        last_name=attributes['last_name']
    )
    StudentUseCaseDI.student_update().execute(student_update_input, transaction_id)


"""
{
    "transaction_id": "04b1aeec-8855-4f43-bb8c-7eef8ef15f8d",
    "event": "pepe.question.create.start",
    "occurred_on": "2019-04-25T02:02:37.109Z",
    "timestamp": 1556157757109,
    "attributes": {
        "id": "question_id",
        "title": "pregunta 1",
        "author": "jose"
    },
    "meta": {
        "server": "pepe-api"
    }
}
"""


class EventHandler(Base):
    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        event = req.media.get('event')
        attributes = req.media.get('attributes')
        transaction_id = req.media.get('transaction_id')

        if event == 'app.user.create.end':
            app_user_create_end(attributes, transaction_id)
            return 'ok'

        if event == 'app.user.update.end':
            app_user_update_end(attributes, transaction_id)
            return 'ok'

        return 'no esta definido el evento: {}'.format(event)
