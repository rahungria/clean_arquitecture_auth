from auth_service import entities
from auth_service.use_cases.ports import user_db
from auth_service.shared.request_error import RequestError
from auth_service.shared import db_errors


class UserDBAdapter(user_db.UserDB):
    '''
    DB Adapter/Wrapper for User entity
    '''
    INSERT_Q = "INSERT INTO public.user(username, password) VALUES (%(username)s, %(password)s) RETURNING *;"
    SELECT_Q = "SELECT * FROM public.user WHERE username=%(username)s;"
    # TODO page lists
    LIST_Q = "SELECT * FROM public.user ORDER BY last_access DESC;"

    def insert(self, username: str, password: bytes):
        con = self.db.get_connection()
        with con:
            with con.cursor() as c:
                try:
                    c.execute(
                        self.INSERT_Q,
                        {'username': username, 'password': password}
                    )
                except db_errors.ClientError as e:
                    raise RequestError(str(e), 400)
                except db_errors.ServerError as e:
                    raise RequestError(str(e), 500)
                data = c.fetchone()
                _username, created, la, pw = data
            return entities.make_user(
                _username,
                bytes(pw),
                created,
                la
            )

    def retrieve(self, username: str):
        con = self.db.get_connection()
        with con:
            with con.cursor() as c:
                try:
                    c.execute(
                        self.SELECT_Q,
                        {'username': username}
                    )
                except db_errors.ClientError as e:
                    raise RequestError(str(e), 400)
                except db_errors.ServerError as e:
                    raise RequestError(str(e), 500)
                data = c.fetchone()
                if not data:
                    raise RequestError("User not Found", 404)
                _username, created, la, pw = data
            return entities.make_user(
                _username,
                bytes(pw),
                created,
                la
            )

    def list(self):
        con = self.db.get_connection()
        with con:
            with con.cursor() as c:
                try:
                    c.execute(self.LIST_Q)
                except db_errors.ClientError as e:
                    raise RequestError(str(e), 400)
                except db_errors.ServerError as e:
                    raise RequestError(str(e), 500)
                users = c.fetchall()
            return [
                entities.make_user(username, bytes(pw), created, last_access)
                for (username, created, last_access, pw) in users
            ]
