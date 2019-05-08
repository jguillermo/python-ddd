import uuid
from abc import ABC, abstractmethod


class EventMessage:
    _transaction_id = None

    def __init__(self, name, attributes, transaction_id=None) -> None:
        if transaction_id is None:
            self.change_transaction(uuid.uuid4().__str__())
        else:
            self.change_transaction(transaction_id)

        self._name = name
        self._attributes = attributes
        self._meta = None

    def change_transaction(self, transaction_id):
        self._transaction_id = transaction_id

    def toExport(self):
        message = {
            "transaction_id": self._transaction_id,
            "name": self._name,
            "attributes": self._attributes
        }

        if self._meta is not None:
            message["meta"] = self._meta

        return message


class Event(ABC):
    @abstractmethod
    def publish(self, event_message: EventMessage):
        pass
