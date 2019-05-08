class CORSMiddleware(object):

    def process_request(self, req, resp):
        allowed_origins = '*'
        allowed_headers = 'Content-Type,Authorization,Platform'
        allowed_methods = 'HEAD, GET, POST, PUT, PATCH, DELETE, OPTIONS'
        origin = req.get_header('Origin', default='*')
        header = {
            'Access-Control-Allow-Headers': allowed_headers,
            'Access-Control-Allow-Methods': allowed_methods
        }
        if origin in allowed_origins:
            header['Access-Control-Allow-Origin'] = origin
        if '*' in allowed_origins:
            header['Access-Control-Allow-Origin'] = '*'

        resp.set_headers(header)
