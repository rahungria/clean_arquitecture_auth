from datetime import datetime


class User:
    '''
    User model

    name -- string

    password -- hashed hex (bytes)

    created -- time of creation

    last_access -- last time of any use_case by user
    '''
    def __init__(
        self,
        username: str,
        password: bytes,
        created: datetime,
        last_access: datetime
    ):
        self.username = username
        self.password = password
        self.created = created
        self.last_access = last_access
        self.validate()

    # TODO validate
    def validate(self):
        pass

    def to_dict(self):
        return dict(
            username=self.username,
            created=self.created.timestamp(),
            last_access=self.last_access.timestamp()
        )


def build_make_user():
    '''
    Injects dependencies (in kwargs) into user model factory
    '''
    def make_user(
        username: str,
        password: bytes, created:
        datetime,
        last_access: datetime
    ) -> User:
        return User(
            username=username,
            password=password,
            created=created,
            last_access=last_access
        )
    return make_user
