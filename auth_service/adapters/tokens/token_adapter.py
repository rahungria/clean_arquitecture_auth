from auth_service.use_cases import ports


class JWTTokenAdapter(ports.TokenPort):
    '''
    JWT implementation of token abstract port
    '''
    def encode(self, payload: dict) -> bytes:
        return self.token_impl.encode(payload)

    def decode(self, token: bytes) -> dict:
        return self.token_impl.decode(token)
