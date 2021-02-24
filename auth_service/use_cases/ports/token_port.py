from abc import ABC, abstractmethod
from auth_service.main.tokens.abstract_token import AbstractToken

class TokenPort(ABC):
    '''
    Abstract Port to use for token encoding/decoding

    must inject 'conf', 'token_adapter' into constructor

    encode(payload: dict) -> str

    decode(token: str) -> dict
    '''
    def __init__(self, token_impl: AbstractToken) -> None:
        self.token_impl = token_impl

    @abstractmethod
    def encode(self, payload: dict) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def decode(self, token: bytes) -> dict:
        raise NotImplementedError