from bootstrap.container import AdapterSqlAlchemyDI


class SQLAlchemySessionManager:
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def process_request(self, req, resp, **kwargs):
        obj_session = AdapterSqlAlchemyDI.alchemy_session()
        obj_session.close()


    def process_response(self, req, resp, resource, req_succeeded):

        obj_session = AdapterSqlAlchemyDI.alchemy_session()
        obj_session.close()
