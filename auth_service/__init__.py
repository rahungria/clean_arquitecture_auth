import flask


app = flask.Flask(__name__)

from auth_service.main.views import *
