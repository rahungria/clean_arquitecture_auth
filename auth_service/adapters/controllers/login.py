from auth_service import use_cases


def login(username: str, password: str):
    return use_cases.login_user(username, password)
