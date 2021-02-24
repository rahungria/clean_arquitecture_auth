import jwt

from . import abstract_token


class JsonWebToken(abstract_token.AbstractToken):
    '''
    Concrete JWT lib wrapper
    '''
    def encode(self, payload: dict) -> bytes:
        return jwt.encode(
            payload,
            self.conf.SECRET_KEY,
            self.conf.TOKEN_ALG
        )

    def decode(self, token: bytes) -> dict:
        return jwt.decode(
            token,
            self.conf.SECRET_KEY,
            self.conf.TOKEN_ALG
        )
