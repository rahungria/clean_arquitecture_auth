from auth_service import use_cases


def signup(username: str, password: str):
    return use_cases.create_users(username, password)
