import bcrypt

from auth_service.adapters.db import user_db
from auth_service.adapters.tokens import token

from .user.create_user import make_create_user
from .user.list_users import make_list_users
from .user.login_user import make_login_user


def hash_algorithm(pw: str):
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

def check_hash(pw: str, hashed: bytes):
    return bcrypt.checkpw(pw.encode('utf-8'), hashed)

create_users = make_create_user(user_db, hash_algorithm)
list_users = make_list_users(user_db)
login_user = make_login_user(user_db, check_hash, token)
