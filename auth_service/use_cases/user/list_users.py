from auth_service.use_cases.ports import user_db


def make_list_users(users_db: user_db.UserDB):
    def list_users():
        return users_db.list()
    return list_users