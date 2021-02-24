from auth_service import use_cases


def get_users():
    return use_cases.list_users()
