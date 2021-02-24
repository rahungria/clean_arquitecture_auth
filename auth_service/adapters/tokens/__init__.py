from . import token_adapter
from auth_service.main.tokens import jwt_token_impl


token = token_adapter.JWTTokenAdapter(jwt_token_impl)
