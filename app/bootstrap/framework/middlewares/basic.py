# -*- coding: utf-8 -*-
import falcon


class Basic(object):

    def process_request(self, req: falcon.Request, resp: falcon.Response):
        print("Im a basic middleware")
