from abc import ABC, abstractmethod


class AbstractToken(ABC):
    '''
    Concrete JWT lib wrapper
    '''
    def __init__(self, conf) -> None:
        self.conf = conf

    @abstractmethod
    def encode(self, payload: dict) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def decode(self, token: bytes) -> dict:
        raise NotImplementedError