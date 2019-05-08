import falcon

from bootstrap.container import EncryptDI
from sdk.exception import UnauthorizedRequest


class SecurityMiddleware:

    def process_resource(self, req: falcon.Request, resp, resource, params):

        req._params['app_unauthorized'] = True

        if req.method == 'OPTIONS':
            return None

        if self.while_list(req.relative_uri, req.method):
            return None
        try:

            token = req.get_header('Authorization', required=False, default='')
            data = EncryptDI.jwt().decode(token)
            req._params['app_data_token'] = data['data']
        except Exception as e:
            req._params['app_unauthorized'] = False

    def while_list(self, url, method):
        list = {
            '/v1/auth/users/login': ['POST','GET'],
            '/v1/pepe/events': ['POST'],
        }

        if url in list and method in list[url]:
            return True

        return False
