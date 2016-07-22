from . import api
from application import db
from application.models.user import User

@api.route("/")
def heool():
    return "hello woohwa"
