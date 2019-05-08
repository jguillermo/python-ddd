from os import environ
from dotenv import load_dotenv
from sdk.adapter.config.base import BaseConfig


class FileConfig(BaseConfig):

    def __init__(self):
        try:
            load_dotenv('/app/config/config.env')
            self._validate('DATABASE')
            self._validate('DATABASE_LOG')
            self._validate('FIREBASE_KEY')

            database_url = environ.get('DATABASE')
            database_log = True if environ.get('DATABASE_LOG') == 'TRUE' else False
            firebase_key = environ.get('FIREBASE_KEY')
            event_url = environ.get('EVENT_URL')

            self._config = {
                'database': {
                    'url': database_url,
                    'log': database_log
                },
                'services': {
                    'host_base': '',
                    'rest': {
                        'ms_location': '',
                        'ms_user': ''
                    }
                },
                'aws': {
                    's3': 'lll'
                },
                'firebase': {
                    'key': firebase_key
                },
                'event_url': event_url
            }
        except Exception as e:
            print(str(e))
            raise e

    def _validate(self, value):
        if environ.get(value) is None:
            raise Exception('No existe la variable: {}'.format(value))
