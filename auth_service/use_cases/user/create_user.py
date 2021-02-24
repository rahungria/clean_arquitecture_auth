from typing import Callable
from auth_service.use_cases.ports import user_db


def make_create_user(user_db: user_db.UserDB, hash_alg: Callable[[str], bytes]):
    '''
    Factory method for method to create users

    user_db -- interface of db

    hash_alg -- callable that returns a hash (bytes) from a string
    '''
    def create_user(username: str, password: str):
        hashed_pw = hash_alg(password)
        return user_db.insert(username, hashed_pw)

    return create_user
