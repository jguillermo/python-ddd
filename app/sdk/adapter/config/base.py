# -*- coding: utf-8 -*-


class BaseConfig(object):

    _config = None

    def get_all(self):
        try:
            return self._config
        except Exception as e:
            raise e

    def get_key(self, key):
        try:
            return self._config[key]
        except Exception as e:
            raise e
