from auth_service.main.conf import conf
from .jwt_token import JsonWebToken

jwt_token_impl = JsonWebToken(conf)
