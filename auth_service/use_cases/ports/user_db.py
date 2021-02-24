from abc import ABC, abstractmethod

from auth_service.main.db import abstract_connection as abs_c
import auth_service.entities.user as user


class UserDB(ABC):
    '''
    User entity db adapter abstract interface for only the given use cases

    list -- () -> User[]

    retrieve -- (username: str) -> User

    insert -- (username: str, password: str) -> User
    '''
    def __init__(self, db_manager: abs_c.AbstractConnectionManager) -> None:
        self.db = db_manager

    @abstractmethod
    def list(self) -> list[user.User]:  # type: ignore
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, username) -> user.User:  # type: ignore
        raise NotImplementedError

    @abstractmethod
    def insert(self, username: str, password: bytes) -> user.User:  # type: ignore
        raise NotImplementedError


