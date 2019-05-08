import requests

from sdk.adapter.config.base import BaseConfig
from sdk.adapter.event import Event, EventMessage


class ApiWateway(Event):

    def __init__(self, config: BaseConfig) -> None:
        self.event_url = config.get_key('event_url')

    def publish(self, event_message: EventMessage):
        try:
            if self.event_url=='localhost':
                return True

            r = requests.post(self.event_url, json=event_message.toExport())
            print('se mando un evento')
        except Exception as e:
            print('no se puede enviar eventos')
            print(e)
