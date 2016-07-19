from . import api
from application import db

@api.route("/")
def heool():
    return "hello woohwa"
