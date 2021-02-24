from typing import Callable

from auth_service.use_cases import ports
from auth_service.shared import request_error


def make_login_user(
    user_db: ports.UserDB,
    check_hash: Callable[[str, bytes], bool],
    token_port: ports.TokenPort
):
    def login_user(username: str, password: str):
        user = user_db.retrieve(username)
        valid = check_hash(password, user.password)
        if valid:
            return token_port.encode(
                {
                    'username': user.username,
                    'last_access': user.last_access.timestamp()
                }
            )
        else:
            raise request_error.RequestError("Invalid Credentials", 401)
    return login_user
