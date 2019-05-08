from abc import ABC, abstractmethod

class EncryptBase(ABC):
    @abstractmethod
    def encode(self, data):
        pass

    @abstractmethod
    def decode(self, jwt_txt):
        pass
