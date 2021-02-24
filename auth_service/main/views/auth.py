from auth_service.shared.request_error import RequestError
from flask import request
import auth_service

from auth_service.adapters.controllers import signup as signup_controller
from auth_service.adapters.controllers import login as login_controller
from auth_service.adapters.controllers import get_users as get_users_controller


app = auth_service.app


# TODO decorator for Request Error Try/Catch wrapping
@app.route('/api/auth/signup/', methods=['POST'])
def signup():
    try:
        try:
            post_data = request.get_json()
            user = signup_controller.signup(
                post_data['username'],
                post_data['password']
            )
            return {'username': user.username}, 201
        except KeyError as e:
            raise RequestError(str(e), 400)
    except RequestError as e:
        return {'error': e.msg}, e.status_code


@app.route('/api/auth/login/', methods=['POST'])
def login():
    try:
        post_data = request.get_json()
        token = login_controller.login(post_data['username'], post_data['password'])
        return {"token": token}, 200
    except RequestError as e:
        return {'error': e.msg}, e.status_code


@app.route('/api/auth/users/', methods=['GET'])
def list_users():
    try:
        users = get_users_controller.get_users()
        return {'users': [user.to_dict() for user in users]}, 200
    except RequestError as e:
        return {'error': e.msg}, e.status_code
